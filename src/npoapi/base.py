import abc
import codecs
import copy
import dataclasses
import http
import logging
import os
import sys
import urllib.request
from enum import Enum
from typing import Dict, List, Optional, Union

from urllib3.exceptions import NameResolutionError
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import npoapi
from npoapi.data.poms import NS_MAP


def declare_namespaces():
    pass


from importlib import reload

declare_namespaces()


class Binding(Enum):
    PYXB = 1  # deprecated?
    XSDATA = 2


import argparse

#
DEFAULT_BINDING = Binding.XSDATA


class NpoApiBase:
    """Base class for all api client (both backend and frontend)"""

    __author__ = "Michiel Meeuwissen"
    __metaclass__ = abc.ABCMeta
    EPILOG = """
    DEBUG=true and ENV=<test|acc|prod> environment variables are recognized.
    Credentials are read from a config file. If such a file does not exist it will offer to create one.
    """

    def __init__(self, env: str = None, debug: bool = False, accept: str = None, interactive: bool = True):
        """
        Initializes logging, env-settings, and default accept headers.
        """
        self.code = None

        logging.basicConfig(format="%(levelname)s %(message)s")
        self.logger = logging.getLogger("Npo")
        self.debug(debug)
        self._env = env
        self.actualenv = None
        self.env(env)
        self._accept = accept
        self.interactive = interactive
        self.settings = {}
        self.response_headers = False
        self.write_count = 0

    @abc.abstractmethod
    def env(self, e):
        """ "Sets environment"""
        self._env = e
        self.actualenv = self._env if self._env else "acc"
        return self

    def debug(self, arg=True):
        self.logger.setLevel(level=logging.DEBUG if arg else logging.INFO)
        return self

    def accept(self, arg=None):
        if arg:
            self._accept = arg
        else:
            first = next(iter(self.accept_choices()))  #
            self._accept = self.accept_choices()[first]
        return self._accept

    def read_environmental_variables(self):
        if self._env is None:
            if "ENV" in os.environ:
                self.env(os.environ["ENV"])
            else:
                self.env("acc")

        if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
            self.debug()

        return self

    def configured_login(
        self, read_environment=False, create_config_file=False, config_dir=None, default_config_dirs=True
    ):
        """
        Logs in using configuration file. Considered using json (no comments-> unusable) or configparser (nearly properties, but headings are required..)
        So, now it simply parses the file itself.
        :param create_config_file: If there is no existing config file, offer to create one
        :param read_environment: If this is set to true, shel environment variables like DEBUG and ENV will be recognized
        :param config_dir: Directory to search config file in
        :param default_config_dirs: Whether to use the default config dir location
        """
        if read_environment:
            self.read_environmental_variables()

        config_files = self.get_configfiles(config_dir=config_dir, default_config_dirs=default_config_dirs)

        config_file = None
        for file in config_files:
            if os.path.isfile(file):
                config_file = os.path.normpath(file)
                break
            else:
                self.logger.debug("not a file " + file)

        self.settings = {}
        if config_file:
            self.logger.debug("Reading " + str(config_file) + " for env " + self.actualenv)
            properties = self._read_properties_file(config_file)
            self._read_settings_from_properties(properties)

        if not config_file and create_config_file:
            print("No configuration file (%s) found. " % ",".join(config_files))

        if self.logger.isEnabledFor(logging.DEBUG):
            settings_for_log = copy.copy(self.settings)
            self.anonymize_for_logging(settings_for_log)
            self.logger.debug("settings" + str(settings_for_log))

        self.logger.debug("Reading settings")

        return self

    def get_setting(self, name: str, description, write_settings=True, write_silent=False) -> str:
        if not (name in self.settings):
            if name.lower() in self.settings:
                value = self.settings[name.lower()]
                del self.settings[name.lower()]
            else:
                if self.interactive:
                    value = input(description + "?: ")
                else:
                    raise ValueError("No setting found " + name.lower())
            self.settings[name] = value
            if write_settings and self.interactive:
                self._write_settings(write_silent=write_silent)
        return self.settings[name]

    @staticmethod
    def get_configfiles(config_dir=None, default_config_dirs=True) -> List[str]:
        current_script_dir = os.path.dirname(sys.argv[0])
        config_files = []
        if default_config_dirs:
            config_files = [
                os.path.join(os.path.expanduser("~"), "conf", "creds.properties"),
                os.path.join(current_script_dir, "..", "..", "..", "creds.properties"),
                os.path.join(current_script_dir, "..", "..", "..", "creds.sh"),
                os.path.join(current_script_dir, "creds.properties"),
            ]

        if not config_dir is None:
            config_files.insert(0, os.path.join(config_dir, "creds.properties"))
        return config_files

    def get_config_file(self, config_dir=None):
        config_file = None
        for file in self.get_configfiles(config_dir=config_dir):
            config_file = os.path.normpath(file)
            if os.access(os.path.dirname(config_file), os.W_OK):
                self.logger.debug("Found " + config_file)
                break
            else:
                self.logger.debug("Not writeable " + config_file)
                config_file = None
        return config_file

    def _write_settings(self, config_dir=None, write_silent=False):
        config_file = self.get_config_file(config_dir=config_dir)

        if config_file:
            with open(str(config_file), "w") as f:
                f.write("# Automatically generated by " + __file__ + "\n")
                for key in self.settings:
                    if len(key.split(".")) == 1:
                        f.write(key + "=" + self.settings[key] + "\n")
                        f.write(key + "." + self.actualenv + "=" + self.settings[key] + "\n")
                    if len(key.split(".")) == 2:
                        f.write(key + "=" + self.settings[key] + "\n")
            if not write_silent:
                self.logger.info("Wrote %s" % str(config_file))
            self.write_count += 1
        else:
            config_files = self.get_configfiles(config_dir=config_dir)
            self.logger.warning("Configuration could not be saved since no file of %s is writable" % str(config_files))

    def _read_properties_file(self, config_file, properties=None) -> Dict[str, str]:
        if properties is None:
            properties = {}
        with open(config_file, "r") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith("#"):
                    try:
                        key, value = l.split("=", 1)
                        value = value.strip('" \t')
                        if value.startswith("system:"):
                            split = value[len("system:") :].split(":", 1)
                            value = os.getenv(split[0])
                            if value is None:
                                value = split[1]
                        properties[key] = value
                    except Exception as e:
                        self.logger.error(l + ":" + str(e))
        return properties

    def _read_settings_from_properties(self, properties):
        for key, value in properties.items():
            split = key.split(".", 2)
            if len(split) == 1:
                self.settings[key.strip()] = value.strip('" \t')
        for key, value in properties.items():
            split = key.split(".", 2)
            if len(split) == 2:
                usedkey, e = split[0], split[1]
                if e == self.actualenv:
                    self.settings[usedkey.strip()] = value.strip('" \t')
                    self.logger.debug("%s %s %s %s", e, usedkey, key, value)
        return self.settings

    @staticmethod
    def anonymize_for_logging(settings_for_log):
        for key, vale in settings_for_log.items():
            if key in ["user", "pages_user", "parkpost_user"]:
                settings_for_log[key] = settings_for_log[key].split(":", 1)[0] + ":xxx"
            if key.endswith("secret"):
                settings_for_log[key] = "xxx"

    def command_line_client(
        self, description=None, read_environment=True, create_config_file=True, exclude_arguments=None
    ):
        """Configure this api client as a command line client. I.e. create an argument parser with common arguments
        and add support for reading config files (e.g. from ~/conf/creds.properties
        """
        self.common_arguments(description=description, exclude_arguments=exclude_arguments)
        return self.configured_login(read_environment=read_environment, create_config_file=create_config_file)

    def add_argument(self, *args, **kwargs):
        self.argument_parser.add_argument(*args, **kwargs)

    def accept_choices(self) -> Dict[str, str]:
        return {"json": "application/json", "xml": "application/xml"}

    def common_arguments(self, description=None, exclude_arguments=None):
        if exclude_arguments is None:
            exclude_arguments = {}
        parent_args = argparse.ArgumentParser(add_help=False)
        parent_args.add_argument("-v", "--version", action="store_true", help="show current version")
        if not "accept" in exclude_arguments:
            parent_args.add_argument("-a", "--accept", type=str, default=None, choices=self.accept_choices().keys())
        parent_args.add_argument(
            "-e", "--env", type=str, default=self._env, choices={"test", "acc", "prod", "localhost"}
        )
        parent_args.add_argument(
            "-u",
            "--url",
            type=str,
            default=None,
            help="The URL of the API which this client communicates with. This is an alternative to --env",
        )
        parent_args.add_argument("-c", "--createconfig", action="store_true", help="Create config")
        parent_args.add_argument("-d", "--debug", action="store_true", help="Switch on debug logging")
        parent_args.add_argument("-H", "--headers", action="store_true", help="Show relevant response headers")

        filtered_argv = []
        i = 0
        while i < len(sys.argv):
            a = sys.argv[i]
            if a in ["-d", "--debug", "-c", "--createconfig", "-v", "--version", "-H", "--headers"]:
                filtered_argv.append(a)
            if a in ["-e", "--env"]:
                filtered_argv.append(a)
                i += 1
                filtered_argv.append(sys.argv[i])
            if a in ["-u", "--url"]:
                filtered_argv.append(a)
                i += 1
                filtered_argv.append(sys.argv[i])
            i += 1
        pargs = parent_args.parse_args(filtered_argv)
        self.debug(pargs.debug)
        self.env(pargs.env)
        self.response_headers = pargs.headers

        if pargs.url:
            self.env(pargs.url)
        if pargs.version:
            print(npoapi.__version__)
            exit(0)
        self.argument_parser = argparse.ArgumentParser(
            description=description, parents=[parent_args], epilog=NpoApiBase.EPILOG
        )
        return self

    def parse_args(self):
        args = self.argument_parser.parse_args()
        self.debug(args.debug)
        if "accept" in args and args.accept:
            self.accept(self.accept_choices().get(args.accept))
        else:
            self.accept()
        return args

    def get_response(
        self, req, url: str, ignore_not_found: bool = False, timeout: int = None
    ) -> Optional[http.client.HTTPResponse]:
        """Error handling around urllib.request.urlopen

        :param ignore_not_found Whether status 404 should be logged as an error
        :param timeout Timeout in seconds

        """
        summary = "%s %s" % (req.method if hasattr(req, "method") else "'GET'" if not req.data else "'POST'", url)
        try:
            self.logger.debug("Executing %s", summary)
            response = urllib.request.urlopen(req, timeout=timeout)
            self.code = response.getcode()
            self.logger.debug("headers: " + str(response.headers))
            if self.response_headers:
                self.logger.info("selector: %s " % (req.selector))
                for h, v in response.getheaders():
                    lowerh = h.lower()
                    if lowerh.startswith("x-npo-warning"):
                        self.logger.warning("%s: %s" % (h, v))
                    elif lowerh.startswith("x-npo-"):
                        self.logger.info("%s: %s" % (h, v))
            else:
                for h, v in response.getheaders():
                    lowerh = h.lower()
                    if lowerh.startswith("x-npo-warning"):
                        self.logger.warning("%s" % (v))
            self.logger.debug("response code: " + str(response.getcode()))
            self.logger.debug("response headers: " + str(response.getheaders()))
            return response
        except urllib.error.URLError as ue:
            error_type = str(type(ue))
            self.logger.debug("headers: %s" % (str(ue.headers) if hasattr(ue, "headers") else "NONE"))
            if ignore_not_found and ue.code == 404:
                self.logger.debug("%s: %s: %s (%s)", url, summary, ue.reason, error_type)
                self.code = 404
                return None
            if type(ue.reason) is str:
                self.logger.error("%s -> %d: %s: %s (%s)", url, ue.code, summary, ue.reason, error_type)
                self.code = ue.code
            else:
                self.logger.error("%s: %s: %s %s (%s)", url, ue.reason.errno, summary, ue.reason.strerror, error_type)
                self.code = ue.reason.errno
            if hasattr(ue, "read"):
                self.logger.error("%s: %s", url, ue.read().decode("utf-8"))
            return None
        except urllib.error.HTTPError as he:
            self.code = he.code
            self.logger.error("%s: %s %s: %s\n%s", url, summary, he.code, he.msg, he.read().decode("utf-8"))
            return None

    def data_to_bytes(self, data, content_type: str = None) -> [bytearray, str]:
        return npoapi.utils.data_to_bytes(data, content_type)

    def write_response(self, response: http.client.HTTPResponse, buffer_size=1024, capture=False) -> Union[None, str]:
        buffer = response.read(buffer_size)
        count = 0
        if capture:
            result = ""
        else:
            result = None
        while len(buffer) > 0:
            s = buffer.decode("utf-8")
            if capture:
                result += s
            sys.stdout.write(s)
            sys.stdout.flush()
            buffer = response.read(buffer_size)
            count += 1

        response.close()
        return result

    @staticmethod
    def isfile(string: str) -> bool:
        return npoapi.utils.isfile(string)

    def data_or_from_file(self, data: str) -> str:
        """"""
        if os.path.isfile(data):
            self.logger.debug("" + data + " is file, reading it in")
            with codecs.open(data, "r", "utf-8") as myfile:
                data = myfile.read()
                self.logger.debug("Found data " + data)
        else:
            if data == "-":
                data = sys.stdin.read()
            self.logger.debug("" + data + " is not a file")
        return data

    def to_object(self, data: str, validate=False, binding=DEFAULT_BINDING) -> Union[object]:
        try:
            return npoapi.utils.to_object(data, validate, binding)
        except Exception as e:
            self.logger.info("Couldn't transform to object %s" % data)
            self.logger.error(str(e))
            return None

    def to_object_or_none(self, data: str, validate=False, binding=DEFAULT_BINDING) -> object:
        import xml

        import xsdata

        try:
            return self.to_object(data, validate, binding=binding)
        except (xml.sax._exceptions.SAXParseException, xsdata.exceptions.ParserError) as e:
            self.logger.debug("Not xml")
            return None

    def exit_code(self) -> int:
        if self.code is None or 200 <= self.code < 300:
            return 0
        return self.code // 100

    def exit(self, message: str = None):
        if message:
            self.logger.error(message)
        sys.exit(self.exit_code())

    def pretty_xml(self, string: str) -> str:
        import xml.parsers.expat
        from xml.dom.minidom import parseString

        try:
            return parseString(string).toprettyxml(indent="  ")
        except xml.parsers.expat.ExpatError as e:
            self.logger.error(e)
            return string

    @abc.abstractmethod
    def info(self):
        return "ABSTRACT"
