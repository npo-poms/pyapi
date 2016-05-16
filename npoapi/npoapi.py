import base64
import hashlib
import hmac
import json
import os
import urllib.request
from email import utils
import sys

from npoapi.base import NpoApiBase


class NpoApi(NpoApiBase):
    EPILOG = """
    DEBUG=true and ENV=<dev|test|prod> environment variables are recognized.
    Credentials are read from a config file. If such a file does not exist it will offer to create one.
    """

    def __init__(self, key: str = None, secret: str = None, env: str = None, origin: str = None, email: str = None,
                 debug: bool = False, accept: str = None):
        """
        Instantiates a client to the NPO Frontend API
        """
        super().__init__(env, debug, accept)
        self.key, self.secret, self.origin = key, secret, origin

    def login(self, key, secret):
        self.key = key
        self.secret = secret
        return self

    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "https://rs.poms.omroep.nl/v1"
        elif e == None or e == "test":
            self.url = "https://rs-test.poms.omroep.nl/v1"
        elif e == "dev":
            self.url = "https://rs-dev.poms.omroep.nl/v1"
        elif e == "localhost":
            self.url = "http://localhost:8070/v1"
        else:
            self.url = e
        return self

    def create_config(self, settings,):
        """
        """
        settings["apikey"] = input("Your NPO api key?: ")
        settings["secret"] = input("Your NPO api secret?: ")
        settings["origin"] = input("Your NPO api origin?: ")
        return self

    def read_settings(self, settings):
        """
        """


        self.login(settings["apikey"], settings["secret"])
        if "origin" in settings:
            self.origin = settings["origin"]

    def anonymize_for_logging(self, settings_for_log):
        if 'secret' in settings_for_log:
            settings_for_log['secret'] = "xxx"
        if 'user' in settings_for_log:
            settings_for_log['user'] = settings_for_log['user'].split(":", 1)[0] + ":xxx"
        return

    def info(self):
        return self.key + "@" + self.url

    def authenticate(self, uri=None, now=utils.formatdate()):
        message = "origin:" + self.origin + ",x-npo-date:" + now + ",uri:/v1" + uri
        self.logger.debug("message: " + message)
        encoded = base64.b64encode(
            hmac.new(self.secret.encode('utf-8'), msg=message.encode('utf-8'), digestmod=hashlib.sha256).digest())
        return "NPO " + self.key + ":" + encoded.decode('utf-8'), now

    def _get_url(self, path, params=None):
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
        authorization, date = self.authenticate(path_for_authentication)
        req.add_header("Authorization", authorization)
        req.add_header("X-NPO-Date", date)
        req.add_header("Origin", self.origin)

        self.logger.debug("url: " + str(req.get_full_url()))

    @staticmethod
    def _get_data(data=None):
        if type(data) == str:
            try:
                json_object = json.JSONDecoder().decode(data)
                return json.JSONEncoder().encode(json_object).encode("UTF-8"), "application/json"
            except json.JSONDecodeError:
                return data.encode("UTF-8"), "application/xml"



        return None,None

    def request(self, path, params=None, accept=None, data=None):
        response = self.stream(path, params, accept, data)
        if response:
            return response.read().decode('utf-8')
        else:
            return ""


    def stream(self, path, params=None, accept=None, data=None):
        if data:
            if os.path.isfile(data):
                self.logger.debug("" + data + " is file, reading it in")
                with open(data, 'r') as myfile:
                    data = myfile.read()
                    self.logger.debug("Found data " + data)

        url, path_for_authentication = self._get_url(path, params)
        d, ct = self._get_data(data)
        req = urllib.request.Request(url, data=d)

        if ct:
            req.add_header("Content-Type", ct)

        self._authentication_headers(req, path_for_authentication)
        req.add_header("Accept", accept if accept else self._accept)
        self.logger.debug("headers: " + str(req.headers))
        return self.get_response(req, url)
        
    



