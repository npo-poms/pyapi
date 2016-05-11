import base64
import codecs
import logging
import os
import subprocess
import sys
import threading
import urllib.request

import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.sax.saxutils import escape

import pytz

from npoapi.base import NpoApiBase

import importlib.util

def declare_namespaces():
    pyxb_loader = importlib.util.find_spec("pyxb")
    if pyxb_loader is not None:
        import pyxb.utils.domutils
        from npoapi.xml import mediaupdate
        from npoapi.xml import media
        from npoapi.xml import shared
    
        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(mediaupdate.Namespace)
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(media.Namespace, 'media')
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(shared.Namespace, 'shared')
    
declare_namespaces()

class MediaBackend(NpoApiBase):
    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__(env, debug, accept)
        self.email = email
        self.authorizationHeader = None

    def create_config(self, settings, ):
        """
        """
        user = input("Your NPO backend user?: ")
        password = input("Your NPO backend password?: ")
        settings["user"] = user + ":" + password
        return self

    def read_settings(self, settings):
        """
        """
        if "user" in settings:
            self.user = settings["user"]
            if ":" in self.user:
                self.password = self.user.split(":", 2)[1]
                self.user = self.user.split(":", 2)[0]
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

    namespaces = {'update': 'urn:vpro:media:update:2009'}


    def get(self, mid):
        """Returns XML-representation of a mediaobject"""
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid)
        return self._get_xml(url)


    def members(self, mid, **kwargs):
        """return a list of all members of a group. As XML objects, wrapped
        in 'items', so you can see the position"""
        return self._members_or_episodes(mid, "members", **kwargs)


    def episodes(self, mid, **kwargs):
        """return a list of all episodes of a group. As XML objects, wrapped
        in 'items', so you can see the position"""
        return self._members_or_episodes(mid, "episodes", **kwargs)

    def delete_member(self, mid, owner_mid):
        self.creds()
        path = "media/media/" + urllib.request.quote(mid) + "/memberOf/" + urllib.request.quote(owner_mid)
        self.delete_to(path)


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

    def _get_xml(self, url):
        try:
            logging.info("getting " + url)
            req = urllib.request.Request(url)
            req.add_header("Accept", "application/xml")
            response = urllib.request.urlopen(req)
        except Exception as e:
            logging.error(url + " " + str(e))
            sys.exit(1)
        return response.read()

    
    def parse_et(self, xml_bytes):
        try:
            return ET.fromstring(xml_bytes)        
        except Exception:
            self.logger.error("Could not parse \n" + xml_bytes.decode(sys.stdout.encoding, "surrogateescape"))


    def parse_minidom(self, xml_bytes):
        try:
            return minidom.parseString(xml_bytes)
        except Exception:
            self.logger.error("Could not parse \n" + xml_bytes.decode(sys.stdout.encoding, "surrogateescape"))


    def anonymize_for_logging(self, settings_for_log):
        if 'password' in settings_for_log:
            settings_for_log['password'] = "xxx"

    def login(self):
        self.logger.debug("Logging in " + self.user)
        password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        username = self.user
        password = self.password
        password_manager.add_password(None, self.url, username, password)
        urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))
        base64string = base64.encodebytes(('%s:%s' % (username, password)).encode()).decode()[:-1]
        self.authorizationHeader = "Basic %s" % base64string
        return self

    def errors(self, mail=None):
        if self.email != mail:
            if mail:
                self.email= mail
                self.logger.debug("Emailing to " + self.email)
            else:
                self.email = None
                self.logger.debug("Not emailing")

    def creds(self):
        if self.authorizationHeader:
            self.logger.debug("Already authorized")
            return
        self.login()

    def post_location(self, mid, programUrl, duration=None, bitrate=None, height=None, width=None, aspectRatio=None, format=None,
                      publishStart=None, publishStop=None):
        if os.path.isfile(programUrl):
            self.logger.debug(programUrl + " seems to be a local file")
            with codecs.open(programUrl, "r", "utf-8") as myfile:
                xml = myfile.read()
        else:
            if not format:
                format = guess_format(programUrl)

            xml = ("<location xmlns='urn:vpro:media:update:2009'" + self.date_attr("publishStart", publishStart) + self.date_attr(
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
            aware = datetime.replace(tzinfo=pytz.UTC)
            return " " + name + "='" + self.date_attr_value(datetime) + "'"
        else:
            return ""

    def date_attr_value(self, datetime_att):
        if datetime_att:
            if type(datetime_att) == str:
                return datetime_att
            else:
                aware = datetime_att.replace(tzinfo=pytz.UTC)
                return aware.strftime("%Y-%m-%dT%H:%M:%SZ")
        return None

    def post_to(self, path, xml, accept="application/xml", **kwargs):
        self.creds()
        url = self.append_params(self.url + path, **kwargs)
        bytes = self.xml_to_bytes(xml)
        req = urllib.request.Request(url, data=bytes)
        self.logger.debug("Posting to " + url)
        return self._request(req, accept=accept)

    def delete_to(self, path, **kwargs):
        self.creds()
        url = self.append_params(self.url + path, **kwargs)
        req = urllib.request.Request(url, method="DELETE")
        self.logger.debug("Deleting " + url)
        return self._request(req)

    def _request(self, req, accept="application/xml"):
        req.add_header("Authorization", self.authorizationHeader)
        req.add_header("Content-Type", "application/xml")
        req.add_header("Accept", accept)
        try:
            response = urllib.request.urlopen(req)
            return response.read().decode()
        except urllib.request.HTTPError as e:
            logging.error(e.read().decode())
            return None

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
        xml = self.get_locations(mid).toprettyxml()
        if location.isdigit():
            args = {"id": location}
            if programUrl:
                args["programUrl"] = programUrl
        else:
            args = {"programUrl": urllib.request.unquote(location)}

        if publishStop:
            args['publishStop'] = self.date_attr_value(publishStop)
        if publishStart:
            args['publishStart'] = self.date_attr_value(publishStart)

        self.logger.debug("Found " + xml)
        location_xml = xslt(xml, self.get_xslt("location_set_publishStop.xslt"), args)
        if location_xml != "":
            self.logger.debug("posting " + location_xml)
            return self.post_to("media/media/" + mid + "/location", location_xml, accept="text/plain")
        else:
            self.logger.debug("no location " + location)
            return "No location " + location
 
    def get_locations(self, mid):
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid) + "/locations"
        return self._get_xml(url)

    def info(self):
        return self.url

    def append_params(self, url, include_errors=True, **kwargs):
        if not kwargs:
            kwargs = {}

        if not "errors" in kwargs and self.email and include_errors:
            kwargs["errors"] = self.email

        sep = "?"
        for key, value in sorted(kwargs.items()):
            url += sep + key + "=" + str(value)
            sep = "&"
        return url


    def xml_to_bytes(self, xml):
        t = type(xml)
        if t == str:
            return xml.encode('utf-8')
        elif t == minidom.Element:
            # xml.setAttribute("xmlns", "urn:vpro:media:update:2009")
            # xml.setAttribute("xmlns:xsi",
            #    "http://www.w3.org/2001/XMLSchema-instance")
            return xml.toxml('utf-8')
        elif t == ET.Element:
            return ET.tostring(xml, encoding='utf-8')
        else:
            raise "unrecognized type " + t


    def _append_element(self, x, element, path=(
            "crid",
            "broadcaster",
            "portal",
            "exclusive",
            "region",
            "title",
            "description",
            "tag",
            "genre",
            "avAttributes",
            "releaseYear",
            "duration",
            "credits",
            "memberOf",
            "ageRating",
            "contentRating",
            "email",
            "website",
            "locations",
            "scheduleEvents",
            "relation",
            "images",
            "asset")):
        t = type(x)
        if t == minidom.Element:
            return self._append_element_minidom(x, element, path)
        elif t == ET.Element:
            return self._append_element_et(x, element, path)
        else:
            return self._append_element_et(ET.fromstring(str(x)), ET.fromstring(str(element)), path)
    
    def _append_element_minidom(self, xml, element, path):
        """Appends an element in the correct location in the given (minidom) xml"""
        index = path.index(element.nodeName)
        for child in xml.childNodes:
            if path.index(child.nodeName) > index:
                xml.insertBefore(element, child)
                return xml
        xml.appendChild(element)
        return xml
    
    def _append_element_et(self, xml, element, path):
        "asdf"
        tagSplit = element.tag.split('}', 2)
        if len(tagSplit) == 2:
            tag = tagSplit[1]
        else:
            tag = tagSplit[0]
        index = path.index(tag)
        for i, child in enumerate(list(xml)):
            if path.index(tag) > index:
                xml.insert(i, element)
                return xml
        xml.insert(len(xml), element)
        return xml
    

lock = threading.Lock()




 
def guess_format(url):
    if url.endswith(".mp4"):
        return "MP4"
    elif url.endswith(".mp3"):
        return "MP3"
    else:
        return "UNKNOWN"



def parkpost_str(xml):
    return parkpost(minidom.parseString(xml).documentElement)


def xslt(xml, xslt_file, params=None):
    if not params:
        params = {}
    args = ["xsltproc"]
    for key, value in params.items():
        args.extend(("--stringparam", key, value))
    args.extend((xslt_file, "-"))
    logging.debug(' '.join(args))
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.write(xml.encode())
    output = p.communicate()
    return str(output[0].decode())



def xml_add_genre(xml, genre_id):
    """Adds a genre to the minidom object"""
    genre_el = xml.ownerDocument.createElement("genre")
    genre_el.appendChild(xml.ownerDocument.createTextNode(genre_id))
    _append_element(xml, genre_el)


def xml_add_duration(xml, duration):
    duration_el = ET.fromstring("<duration xmlns='urn:vpro:media:update:2009'>%s</duration>" % duration)
    _append_element(xml, duration_el)




def post(xml, lookupcrid=False, followMerges=True):
    return post_to("media/media", xml, accept="text/plain", lookupcrid=lookupcrid, followMerges=followMerges)


def find(xml, lookupcrid=False, followMerges=True):
    return post_to("media/find", xml, lookupcrid=lookupcrid, followMerges=followMerges)


def parkpost(xml):
    creds("parkpost:")
    url = target + "parkpost/promo"

    logging.info("posting to " + url)
    req = urllib.request.Request(url, data=xml.toxml('utf-8'))
    return _post(req)


