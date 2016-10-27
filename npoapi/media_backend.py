import codecs
import os
import urllib.request
from xml.dom import minidom
from npoapi.basic_backend import BasicBackend
from npoapi.xml import media, mediaupdate, poms


class MediaBackend(BasicBackend):
    def __init__(self, env:str=None, email:str = None, debug:bool=False, accept:str=None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__(env, email, debug, accept)

    def read_settings(self, settings: dict):
        """
        """
        if "user" in settings:
            self.user = settings["user"]
            if ":" in self.user:
                self.password = self.user.split(":", 2)[1]
                self.user = self.user.split(":", 2)[0]
        if "email" in settings:
            self.email = settings["email"]
        if "parkpost_user" in settings:
            self.parkpost_user = settings["parkpost_user"]
            if ":" in self.parkpost_user:
                self.parkpost_password = self.parkpost_user.split(":", 2)[1]
                self.parkpost_user = self.parkpost_user.split(":", 2)[0]
                self.parkpost_authorization = self.generate_authorization(self.parkpost_user, self.parkpost_password)
        return

    def env(self, e:str):
        super().env(e)
        if e == "prod":
            self.url = "https://api.poms.omroep.nl/"
        elif e == None or e == "test":
            self.url = "https://api-test.poms.omroep.nl/"
        elif e == "dev":
            self.url = "https://api-dev.poms.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8071/rs/"
        else:
            self.url = e
        return self

    def get(self, mid: str, ignore_not_found=False) -> bytearray:
        """Returns XML-representation of a mediaobject"""
        return self.get_from("media/media/" + urllib.request.quote(mid, safe=''), ignore_not_found=ignore_not_found)

    def get_full(self, mid: str, ignore_not_found=False) -> bytearray:
        """Returns XML-representation of a mediaobject"""
        return self.get_from("media/media/" + urllib.request.quote(mid, safe='') + "/full", ignore_not_found=ignore_not_found)

    def get_object(self, mid: str, ignore_not_found=False) -> mediaupdate:
        """Returns pyxb-representation of a mediaobject"""
        return self.to_object(self.get(mid, ignore_not_found), validate=False)

    def get_full_object(self, mid: str, ignore_not_found=False) -> media:
        """Returns pyxb-representation of a mediaobject"""
        return self.to_object(self.get_full(mid, ignore_not_found), validate=False)

    def post(self, update, lookupcrid=True):
        update = self.to_object(update, validate=True)
        return self.post_to("media/media/", update, accept="text/plain", errors=self.email, lookupcrid=lookupcrid)

    def delete(self, mid:str):
        """"""
        return self.delete_from("media/media/" + urllib.request.quote(mid, safe=''))

    def parkpost(self, xml):
        url = self.url + "parkpost/promo"
        req = urllib.request.Request(url, data=self.xml_to_bytes(xml))
        return self._request(req, url, accept="text/plain", authorization=self.parkpost_authorization)

    def find(self, form, writeable=False):
        form = self.to_object(form, validate=True)
        return self.post_to("media/find", form, accept="application/xml", writable=writeable)


    def members(self, mid: str, **kwargs) -> list:
        """return a list of all members of a group. As minidom  XML objects, wrapped
        in 'items', so you can see the position"""
        return self.members_or_episodes(mid, "members", **kwargs)

    def episodes(self, mid, **kwargs) -> list:
        """return a list of all episodes of a group. As minidom XML objects, wrapped
        in 'items', so you can see the position"""
        return self.members_or_episodes(mid, "episodes", **kwargs)

    def delete_member(self, mid, owner_mid):
        path = "media/media/" + urllib.request.quote(mid) + "/memberOf/" + urllib.request.quote(owner_mid)
        self.delete_from(path)

    # private method to implement both members and episodes calls.
    def members_or_episodes(self, mid:str, what:str, max:int=None, batch:int=20, log_progress=False, log_indent="") -> list:
        """Returns a list of minidom objects"""
        self.creds()
        self.logger.debug("loading %s of %s", what, mid)
        result = []
        offset = 0
        b = min(batch, max) if max else batch
        while True:
            sub = "group" if what == "episodes" else "media"
            url = (self.url + 'media/' + sub + '/' + urllib.request.quote(mid, '') + "/" + what + "?max=" + str(b) +
                   "&offset=" + str(offset))
            bytes = self._get_xml(url)
            if bytes:
                xml = minidom.parseString(bytes)
                items = xml.getElementsByTagName('item')
                #result.extend(map(lambda i: poms.CreateFromDOM(i, default_namespace=mediaupdate.Namespace), items))
                result.extend(items)
                if len(items) == 0 or (max and len(result) >= max):
                    break
                if log_progress:
                    if len(items) != len(result):
                        self.logger.info("%s%s of %s: %s (+%s)", log_indent, what, mid, len(result), len(items))
                    else:
                        self.logger.info("%s%s of %s: %s", log_indent, what, mid, len(result))
                offset += b
                # print xml.childNodes[0].toxml('utf-8')
                total = xml.childNodes[0].getAttribute("totalCount")
                self.logger.debug(str(len(result)) + "/" + total + (("/" + str(max)) if max else ""))
            else:
                self.logger.debug("None returned from %s", url)

        return result

    def post_location(self, mid:str, programUrl, duration:str=None, bitrate:int=None, height:int=None, width:int=None, aspectRatio:str=None,
                      format:str=None,
                      publishStart=None, publishStop=None):
        if os.path.isfile(programUrl):
            self.logger.debug(programUrl + " seems to be a local file")
            with codecs.open(programUrl, "r", "utf-8") as myfile:
                xml = myfile.read()
        else:
            if not format:
                format = self.guess_format(programUrl)

            xml = ("<location xmlns='urn:vpro:media:update:2009'" + self.date_attr("publishStart",
                                                                                   publishStart) + self.date_attr(
                "publishStop", publishStop) + ">" +
                   "  <programUrl>" + programUrl + "</programUrl>" +
                   "   <avAttributes>")
            if bitrate:
                xml += "<bitrate>" + str(bitrate) + "</bitrate>"
            if format:
                xml += "<avFileFormat>" + format + "</avFileFormat>"

            if height or width or aspectRatio:
                xml += "<videoAttributes "
                if height:
                    xml += "height='" + str(height) + "' "
                if width:
                    xml += "width='" + str(width) + "' "
                xml += ">"
                if aspectRatio:
                    xml += "<aspectRatio>" + aspectRatio + "</aspectRatio>"
                xml += "</videoAttributes>"

            xml += "</avAttributes>"
            if duration:
                xml += "<duration>" + duration + "</duration>"

            xml += "</location >"

        self.logger.debug("posting " + xml)
        return self.post_to("media/media/" + mid + "/location", xml, accept="text/plain")

    def date_attr(self, name:str, datetime):
        if datetime:
            return " " + name + "='" + self.date_attr_value(datetime) + "'"
        else:
            return ""

    def add_image(self, mid:str, image):
        return self.post_to("media/media/" + mid + "/image", image, accept="text/plain")

    def set_location(self, mid, location, publishStop=None, publishStart=None, programUrl=None):
        locations = poms.CreateFromDocument(self.get_locations(mid)).wildcardElements()
        location_object = None
        for l in locations:
            if type(location) == int or location.isdigit():
                if (l.urn is not None and str(l.urn).endswith(':' + str(location))) and (
                        programUrl is None or str(l.programUrl) == programUrl):
                    location_object = l
                    break
            elif str(l.urn).startswith("urn:vpro:media:location:"):
                if (str(l.urn) == location) and (programUrl is None or str(l.programUrl) == programUrl):
                    location_object = l
                    break
            else:
                if str(l.programUrl) == location:
                    location_object = l
                    break

        if location_object is None:
            # location_object = mediaupdate.locationUpdateType()
            location_object = mediaupdate.CreateFromDocument("""<location xmlns="urn:vpro:media:update:2009">
<programUrl>http://www.vpro.nl/123</programUrl>
<avAttributes>
<avFileFormat>MP4</avFileFormat>
</avAttributes>
</location>""")
            if programUrl is not None:
                location_object.programUrl = programUrl
            elif not location.isdigit():
                location_object.programUrl = location
            else:
                return None
        location_object.avAttributes.avFileFormat = self.guess_format(location_object.programUrl)

        self.logger.debug("no match for %s. Created location." % location)

        self.logger.debug("Processing %s" % location_object)

        if publishStop:
            location_object.publishStop = publishStop
        if publishStart:
            location_object.publishStart = publishStart

        location_xml = location_object.toxml()
        self.logger.debug("Found " + location_xml)
        return self.post_to("media/media/" + mid + "/location", location_xml, accept="text/plain")

    def get_locations(self, mid:str):
        return self.get_sub(mid, "locations")

    def get_images(self, mid:str):
        return self.get_sub(mid, "images")

    def get_sub(self, mid:str, sub: str):
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid) + "/" + sub
        return self._get_xml(url)


    def guess_format(self, url):
        if str(url).endswith(".mp4"):
            return media.avFileFormatEnum.MP4
        elif str(url).endswith(".mp3"):
            return media.avFileFormatEnum.MP3
        else:
            return media.avFileFormatEnum.UNKNOWN
