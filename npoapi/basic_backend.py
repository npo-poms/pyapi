import base64
import importlib.util
import logging
import urllib.request
from xml.dom import minidom

from npoapi.base import NpoApiBase


def declare_namespaces():
    pyxb_loader = importlib.util.find_spec("pyxb")
    if pyxb_loader is not None:
        import pyxb.utils.domutils
        from npoapi.xml import mediaupdate
        from npoapi.xml import pagesupdate
        from npoapi.xml import pages
        from npoapi.xml import media
        from npoapi.xml import shared

        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(mediaupdate.Namespace)
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pagesupdate.Namespace, 'pu')
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pages.Namespace, 'pages')
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(media.Namespace, 'media')
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(shared.Namespace, 'shared')

declare_namespaces()


class BasicBackend(NpoApiBase):
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
            self.url = "https://publish.pages.omroep.nl/"
        elif e == None or e == "test":
            self.url = "https://publish-test.pages.omroep.nl/"
        elif e == "dev":
            self.url = "https://publish-dev.pages.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8071/rs/"
        else:
            self.url = e
        return self


    def errors(self, email):
        self.email = email


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

    def creds(self):
        if self.authorizationHeader:
            self.logger.debug("Already authorized")
            return
        self.login()

    def post_to(self, path, xml, accept="application/xml", **kwargs):
        self.creds()
        url = self.append_params(self.url + path, **kwargs)
        bytes = self.xml_to_bytes(xml)
        req = urllib.request.Request(url, data=bytes)
        self.logger.debug("Posting " + str(bytes) + " to " + url)
        return self._request(req, accept=accept)

    def delete_to(self, path, **kwargs):
        self.creds()
        url = self.append_params(self.url + path, **kwargs)
        req = urllib.request.Request(url, method="DELETE")
        self.logger.debug("Deleting " + url)
        return self._request(req)

    def _get_xml(self, url):
        self.logger.debug("getting " + url)
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/xml")
        response = self.get_response(req, url)
        return response.read()

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

    def info(self):
        return self.url

    def date_attr_value(self, datetime_att):
        if datetime_att:
            if type(datetime_att) == str:
                return datetime_att
            else:
                aware = datetime_att.replace(tzinfo=pytz.UTC)
                return aware.strftime("%Y-%m-%dT%H:%M:%SZ")
        return None

    def append_params(self, url, include_errors=True, **kwargs):
        if not kwargs:
            kwargs = {}

        if not "errors" in kwargs and self.email and include_errors:
            kwargs["errors"] = self.email

        sep = "?"
        for key, value in sorted(kwargs.items()):
            if not value is None:
                url += sep + key + "=" + str(value)
                sep = "&"
        return url


    def xml_to_bytes(self, xml):
        import xml.etree.ElementTree as ET
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
        elif getattr(xml, "toDOM"):
            return xml.toDOM().toxml('utf-8')
        else:
            raise "unrecognized type " + t


