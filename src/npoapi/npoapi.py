import base64
import hashlib
import hmac
import http
import json
import urllib.request
from email import utils
from typing import Optional

from npoapi.base import NpoApiBase


class NpoApi(NpoApiBase):
    """
    Client API for NPO Frontend Api

    """

    __author__ = "Michiel Meeuwissen"

    EPILOG = """
    DEBUG=true and ENV=<test|acc|prod> environment variables are recognized.
    Credentials are read from a config file. If such a file does not exist it will offer to create one.
    """

    def __init__(
        self,
        key: str = None,
        secret: str = None,
        env: str = None,
        origin: str = None,
        debug: bool = False,
        accept: str = None,
        interactive: bool = True,
    ):
        """
        Instantiates a client to the NPO Frontend API
        """
        super().__init__(env=env, debug=debug, accept=accept, interactive=interactive)
        self.key, self.secret, self.origin = key, secret, origin

    def login(self, key, secret, origin=None):
        self.key = key.lstrip()
        self.secret = secret.lstrip()
        if not origin is None:
            self.origin = origin
        return self

    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "https://rs.poms.omroep.nl/v1"
        elif e == "testa":
            self.url = "https://api-server-poms-stack-test.apps.poms.cluster.chp4.io/v1"
        elif e == "acc":
            self.url = "https://rs-acc.poms.omroep.nl/v1"
        elif (e is None and self._env is None) or e == "test":
            self.url = "https://rs-test.poms.omroep.nl/v1"
        elif e == "localhost":
            self.url = "http://localhost:8070/v1"
        else:
            self.url = e
        return self

    def info(self) -> str:
        return self.key + "@" + self.url

    def authenticate(self, uri="", now=utils.formatdate(usegmt=True), interactive=True) -> [str, str]:
        if interactive:
            prev_write_count = self.write_count
            if self.origin is None:
                self.origin = self.get_setting("origin", "Your NPO api origin", interactive, write_silent=True)
            if self.key is None:
                self.key = self.get_setting("apiKey", "Your NPO api key", interactive, write_silent=True)
            if self.secret is None:
                self.secret = self.get_setting("secret", "Your NPO api secret", interactive, write_silent=True)
            if self.write_count > prev_write_count:
                self.logger.info("Wrote config file %s" % self.get_config_file())

        message = "origin:" + self.origin + ",x-npo-date:" + now + ",uri:/v1" + uri
        self.logger.debug("message: " + message)
        encoded = base64.b64encode(
            hmac.new(self.secret.encode("utf-8"), msg=message.encode("utf-8"), digestmod=hashlib.sha256).digest()
        )
        return "NPO " + self.key + ":" + encoded.decode("utf-8"), now

    def _get_url(self, path, params=None) -> [str, str]:
        if not params:
            params = {}

        path_for_authentication = path
        if params.items():
            sep = "?"
            for k, v in sorted(params.items()):
                if v is not None:
                    path += sep + k + "=" + urllib.request.quote(str(v))
                    path_for_authentication += "," + k + ":" + str(v)
                    sep = "&"

        url = self.url + path
        return url, path_for_authentication

    def _authentication_headers(self, req, path_for_authentication):
        authorization, date = self.authenticate(path_for_authentication, interactive=self.interactive)
        req.add_header("Authorization", authorization)
        req.add_header("X-NPO-Date", date)
        req.add_header("Origin", self.origin)

        self.logger.debug("url: " + str(req.get_full_url()))

    def _get_data(self, data: str = None, content_type: str = None) -> [bytearray, str]:
        """Automatically determines the content_type if it is not set"""
        if data is None:
            pass
        elif type(data) == str:
            if content_type is not None:
                return data.encode("UTF-8"), content_type
            try:
                json_object = json.JSONDecoder(strict=False).decode(data)
                return json.JSONEncoder().encode(json_object).encode("UTF-8"), "application/json"
            except json.JSONDecodeError as je:
                if data.startswith("<"):
                    self.logger.debug("Data looks like xml, taking content type accordingly (%s)", str(je))
                    return data.encode("UTF-8"), "application/xml"
                else:
                    self.logger.warn("Data %s could not be parsed as json. Leaving content type unspecified", data)
                    return data.encode("UTF-8"), None
        else:
            self.logger.warn("Input %s is not a string", data)

        return None, None

    def request_or_stream(
        self,
        path: str,
        params=None,
        accept=None,
        data=None,
        content_type: str = None,
        timeout=None,
        ignore_not_found=False,
        stream: bool = False,
    ):
        if stream:
            return self.stream(
                path=path,
                params=params,
                accept=accept,
                data=data,
                content_type=content_type,
                timeout=timeout,
                ignore_not_found=ignore_not_found,
            )
        else:
            return self.request(
                path=path,
                params=params,
                accept=accept,
                data=data,
                content_type=content_type,
                ignore_not_found=ignore_not_found,
            )

    def request(
        self, path, params=None, accept=None, data=None, content_type: str = None, ignore_not_found=False
    ) -> Optional[str]:
        """Executes a request and return the result as a string, or None if not found"""
        response = self.stream(path, params, accept, data, content_type, ignore_not_found=ignore_not_found)
        if response:
            self.logger.debug(response.headers)
            return response.read().decode("utf-8")
        else:
            return None

    def stream(
        self,
        path: str,
        params=None,
        accept=None,
        data=None,
        content_type: str = None,
        timeout=None,
        ignore_not_found=False,
    ) -> Optional[http.client.HTTPResponse]:
        data, content_type = self.data_to_bytes(data, content_type)
        if data is not None:
            data_as_string = data.decode("utf-8")
        else:
            data_as_string = None

        url, path_for_authentication = self._get_url(path, params)

        d, content_type = self._get_data(data_as_string, content_type=content_type)
        req = urllib.request.Request(url, data=d)

        if content_type:
            req.add_header("Content-Type", content_type)

        self._authentication_headers(req, path_for_authentication)
        effective_accept = accept if accept else self._accept
        if effective_accept is not None:
            req.add_header("Accept", effective_accept)
        self.logger.debug("headers: %s" % str(req.headers))
        self.logger.debug("url: %s" % url)
        return self.get_response(req, url, ignore_not_found=ignore_not_found, timeout=timeout)

    def __str__(self) -> str:
        return "frontend api client " + self.url
