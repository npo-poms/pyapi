import base64
import dataclasses
import logging
import urllib.request
from typing import Optional, Tuple
from xml.dom import minidom

import pytz
import pyxb
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from npoapi.base import NpoApiBase, NS_MAP
from npoapi.xml import mediaupdate


class BasicBackend(NpoApiBase):
    """Base class for backend apis. These use basic authentication. Normally communicate via XML."""
    __author__ = "Michiel Meeuwissen"

    def __init__(self, description=None, env=None, email: str = None, debug=False, accept=None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__(env, debug, accept)
        self.user = None
        self.password = None
        self.email = email
        self.url = None
        self.authorizationHeader = None
        self.description = description

    def client(self, user=None, password=None, url=None, email=None):
        """
        Explicitely sets some fields
        """
        self.email = email
        self.user = user
        self.password = password
        self.url = url
        return self

    def get_users(self):
        """Settings keys used for authentication information"""
        return ["user"]

    def env(self, e):
        super().env(e)
        return self

    def errors(self, email):
        self.email = email

    def get_errors(self):
        return self.email or self.settings.get('errors') or self.settings.get('email')

    def login(self):
        """Authenticates if not yet authenticated."""
        if self.authorizationHeader:
            self.logger.debug("Already authenticated")
        else:
            user_key = self.get_users()[0]
            self.authorizationHeader = self._basic_authentication(user_key, "Your " + self.description)
        return self

    def _basic_authentication(self, settings_key, description):
        if not (settings_key in self.settings):
            if self.interactive:
                user = input(description + " user?: ")
                password = input(description + " password?: ")
                self.settings[settings_key] = user + ":" + password
                self._write_settings()
            else:
                raise ValueError("No setting found " + settings_key)

        self.user = self.settings[settings_key]
        password = self.user.split(":", 2)[1]
        user = self.user.split(":", 2)[0]
        self.logger.debug("Logging in " + user)
        return self._generate_basic_authorization(user, password)


    def _generate_basic_authorization(self, username, password):
        password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        if  self.url is None:
            raise Exception("No url configured for " + str(self))
        password_manager.add_password(None, self.url, username, password)
        urllib.request.install_opener(
            urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))
        base64string = base64.encodebytes(('%s:%s' % (username, password)).encode()).decode()[:-1]
        return "Basic %s" % base64string

    def _creds(self):
        """Checks whether authentication information is present in self, and if not make sure it is."""
        if not self._needs_login():
            self.logger.debug("Already authorized")
            return
        self.login()

    def _needs_login(self):
        return not self.authorizationHeader

    def post_to(self, path, xml, accept=None, **kwargs) -> Tuple[Optional[str], Optional[str]]:
        """Post to path on configured server. Add necessary authentication headers"""
        self._creds()
        url = self.append_params(self.url + path, **kwargs)
        if xml is None:
            raise Exception("Cant post without xml")
        bytes = self.xml_to_bytes(xml)
        req = urllib.request.Request(url, data=bytes, method='POST')
        self.logger.debug("Posting " + str(bytes) + " to " + url)
        return self._request(req, url, accept=accept)

    def get_from(self, path:str, accept="application/xml", ignore_not_found=False, **kwargs) -> Tuple[Optional[str], Optional[str]]:
        self._creds()
        _url = self.append_params(self.url + path, include_errors=False, **kwargs)
        req = urllib.request.Request(_url)
        self.logger.debug("Getting from " + _url)
        return self._request(req, _url, accept=accept, ignore_not_found=ignore_not_found)

    def delete_from(self, path: str, **kwargs) -> Tuple[Optional[str], Optional[str]]:
        self._creds()
        url = self.append_params(self.url + path, **kwargs)
        req = urllib.request.Request(url, method="DELETE")
        self.logger.debug("Deleting " + url)
        return self._request(req, url)

    def _get_xml(self, url:str) -> Optional[bytes]:
        """Gets XML (as a byte array) from an URL. So this sets the accept header."""
        self._creds()
        self.logger.debug("getting " + url)
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/xml")
        response = self.get_response(req, url)
        if response:
            return response.read()
        else:
            return None

    def _request(self, req, url, accept=None, needs_authentication=True, authorization=None, ignore_not_found=False) -> Tuple[Optional[str], Optional[str]]:
        if needs_authentication:
            if authorization:
                req.add_header("Authorization", authorization)
            else:
                if not self.authorizationHeader:
                    raise Exception("No user/password configured")
                req.add_header("Authorization", self.authorizationHeader)
        req.add_header("Content-Type", "application/xml")
        req.add_header("Accept", accept or self._accept)
        try:
            response = self.get_response(req, url, ignore_not_found=ignore_not_found)
            if response:
                result = response.read().decode()
                warnings = response.headers.get_all('x-npo-validation-warning')
                if warnings:
                    for w in warnings:
                        self.logger.warning("%s", str(w))
                errors = response.headers.get_all('x-npo-validation-error')
                if errors:
                    for e in errors:
                        self.logger.error("%s", str(e))
                self.logger.debug("Found: %s", result)

                return result, response.headers.get('content-type')
            else:
                return None, None
        except urllib.request.HTTPError as e:
            logging.error(e.read().decode())
            return None, None

    def info(self):
        return self.url

    def date_attr_value(self, datetime_att) -> Optional[str]:
        if datetime_att:
            if type(datetime_att) == str:
                return datetime_att
            else:
                aware = datetime_att.replace(tzinfo=pytz.UTC)
                return aware.strftime("%Y-%m-%dT%H:%M:%SZ")
        return None

    def append_params(self, _url: str, include_errors=True, **kwargs) -> str:
        if not kwargs:
            kwargs = {}

        if include_errors:
            error_mail = self.get_errors()
            if (not "errors" in kwargs or kwargs["errors"] is None) and error_mail:
                kwargs["errors"] = error_mail

        sep = "?"
        for key, value in sorted(kwargs.items()):
            if not value is None:
                _url += sep + key + "=" + urllib.request.quote(str(value))
                sep = "&"
        return _url

    @staticmethod
    def toxml(update: pyxb.binding.basis.complexTypeDefinition) -> bytes:
        "xsi:- xml are not working out of the box.."
        t = type(update)
        if t == mediaupdate.programUpdateType:
            return bytes(update.toxml("utf-8", element_name='program'))
        elif t == mediaupdate.groupUpdateType:
            return bytes(update.toxml("utf-8", element_name='group'))
        elif t == mediaupdate.segmentUpdateType:
            return bytes(update.toxml("utf-8", element_name='segment'))
        else:
            return bytes(update.toxml("utf-8"))

    def xml_to_bytes(self, xml) -> bytes:
        """Accepts xml in several formats, and returns it as a byte array, ready for posting"""
        import xml.etree.ElementTree as ET
        import pyxb

        t = type(xml)
        if t == str:
            xml, content_type = self.data_to_bytes(xml)
            return xml
        elif dataclasses.is_dataclass(xml):
            serializer = XmlSerializer(config=SerializerConfig(pretty_print = False))
            content_type = "application/xml"
            return serializer.render(xml, ns_map=NS_MAP).encode("utf-8")
        elif t == minidom.Element:
            # xml.setAttribute("xmlns", "urn:vpro:media:update:2009")
            # xml.setAttribute("xmlns:xsi",
            #    "http://www.w3.org/2001/XMLSchema-instance")
            return xml.toxml('utf-8')
        elif t == minidom.Document:
            return xml.toxml('utf-8')
        elif t == ET.Element:
            return ET.tostring(xml, encoding='utf-8')
        elif isinstance(xml, pyxb.binding.basis.complexTypeDefinition):
            return self.toxml(xml)
        elif hasattr(xml, "toDOM"):
            return xml.toDOM().toxml('utf-8')
        else:
            raise Exception("unrecognized type " + str(t))


