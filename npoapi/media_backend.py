import base64
import codecs
import os
import urllib.request
from xml.sax.saxutils import escape

from npoapi.basic_backend import BasicBackend
from npoapi.xml import media, mediaupdate, poms


class MediaBackend(BasicBackend):
    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__(env, email, debug, accept)

    def read_settings(self, settings):
        """
        """
        if "user" in settings:
            self.user = settings["user"]
            if ":" in self.user:
                self.password = self.user.split(":", 2)[1]
                self.user = self.user.split(":", 2)[0]
        if "email" in settings:
            self.email = settings["email"]
        return

    def env(self, e):
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

    def get(self, mid):
        """Returns XML-representation of a mediaobject"""
        return self.get_from("media/media/" + urllib.request.quote(mid, safe=''))

    def post(self, update):
        update = self.to_object(update, validate=True)
        return self.post_to("media/media/", update, accept="text/plain", errors=self.email)

    def delete(self, mid):
        """"""
        return self.delete_from("media/media/" + urllib.request.quote(mid, safe=''))

    def find(self, form, writeable=False):
        form = self.to_object(form)
        return self.post_to("media/media/find", form, accept="application/xml", writable=writeable)

    def members(self, mid, **kwargs):
        """return a list of all members of a group. As XML objects, wrapped
        in 'items', so you can see the position"""
        return self._members_or_episodes(mid, "members", **kwargs)

    def episodes(self, mid, **kwargs):
        """return a list of all episodes of a group. As XML objects, wrapped
        in 'items', so you can see the position"""
        return self._members_or_episodes(mid, "episodes", **kwargs)

    def delete_member(self, mid, owner_mid):
        path = "media/media/" + urllib.request.quote(mid) + "/memberOf/" + urllib.request.quote(owner_mid)
        self.delete_from(path)

    # private method to implement both members and episodes calls.
    def _members_or_episodes(self, mid, what, max=None, batch=20):
        self.creds()
        self.logger.info("loading members of " + mid)
        result = []
        offset = 0
        b = min(batch, max) if max else batch
        while True:
            url = (self.url + 'media/group/' + urllib.request.quote(mid, '') + "/" + what + "?max=" + str(b) +
                   "&offset=" + str(offset))
            xml = self._get_xml(url)
            items = xml.getElementsByTagName('item')
            result.extend(items)
            if len(items) == 0 or (max and len(result) >= max):
                break
            offset += b
            # print xml.childNodes[0].toxml('utf-8')
            total = xml.childNodes[0].getAttribute("totalCount")
            self.logger.info(str(len(result)) + "/" + total + (("/" + str(max)) if max else ""))

        return result

    def post_location(self, mid, programUrl, duration=None, bitrate=None, height=None, width=None, aspectRatio=None,
                      format=None,
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
                xml += "<bitrate>" + str(bitrate) + "</bitrate>";
            if format:
                xml += "<avFileFormat>" + format + "</avFileFormat>";

            if height or width or aspectRatio:
                xml += "<videoAttributes "
                if height:
                    xml += "height='" + height + "' "
                if width:
                    xml += "width='" + width + "' "
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

    def date_attr(self, name, datetime):
        if datetime:
            return " " + name + "='" + self.date_attr_value(datetime) + "'"
        else:
            return ""

    def add_image(self, mid, image, image_type="PICTURE", title=None, description=None):
        if os.path.isfile(image):
            with open(image, "rb") as image_file:
                if not title:
                    title = "Image for %s" % escape(mid)
                if not description:
                    description_xml = ""
                else:
                    description_xml = "<description>%s</description>" % escape(description)

                encoded_string = base64.b64encode(image_file.read()).decode("ascii")
                xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <image xmlns="urn:vpro:media:update:2009" type="%s">
      <title>%s</title>
      %s
      <imageData>
        <data>%s</data>
      </imageData>
    </image>
    """ % (image_type, escape(title), description_xml, encoded_string)
                self.logger.debug(xml)
                return self.post_to("media/media/" + mid + "/image", xml, accept="text/plain")

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

    def get_locations(self, mid):
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid) + "/locations"
        return self._get_xml(url)

    def get_images(self, mid):
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid) + "/images"
        return self._get_xml(url)

    def guess_format(self, url):
        if str(url).endswith(".mp4"):
            return media.avFileFormatEnum.MP4
        elif str(url).endswith(".mp3"):
            return media.avFileFormatEnum.MP3
        else:
            return media.avFileFormatEnum.UNKNOWN
