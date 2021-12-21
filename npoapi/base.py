import abc
import argparse
import codecs
import copy
import logging
import os
import sys
import urllib.request
import http

import pyxb
import dataclasses

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import npoapi
from typing import Optional
from typing import List
from typing import Dict
from enum import Enum



def declare_namespaces():
    import pyxb.utils.domutils
    from npoapi.xml import mediaupdate, pageupdate, page, media, shared, api, thesaurus

    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(mediaupdate.Namespace)
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pageupdate.Namespace, 'pu')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(page.Namespace, 'pages')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(media.Namespace, 'media')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(shared.Namespace, 'shared')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(api.Namespace, 'api')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(thesaurus.Namespace, 'gtaa')



NS_MAP={"api": 'urn:vpro:api:2013',
        "update": "urn:vpro:media:update:2009"}



declare_namespaces()

class Binding(Enum):
    PYXB = 1
    XSDATA = 2

class NpoApiBase:
    """Base class for all api client (both backend and frontend)"""
    __author__ = "Michiel Meeuwissen"
    __metaclass__ = abc.ABCMeta
    EPILOG = """
    DEBUG=true and ENV=<dev|test|prod> environment variables are recognized.
    Credentials are read from a config file. If such a file does not exist it will offer to create one.
    """

    def __init__(self, env: str = None, debug: bool = False, accept: str = None, interactive: bool = True):
        """
        Initializes logging, env-settings, and default accept headers.
        """
        self.code = None

        logging.basicConfig(format='%(levelname)s %(message)s')
        self.logger = logging.getLogger("Npo")
        self.debug(debug)
        self._env = env
        self.actualenv = None
        self.env(env)
        self._accept = accept or "application/json"
        self.interactive = interactive
        self.settings = {}
        self.response_headers = False


    @abc.abstractmethod
    def env(self, e):
        """"Sets environment"""
        self._env = e
        self.actualenv = self._env if self._env else "test"
        return self

    def debug(self, arg=True):
        self.logger.setLevel(level=logging.DEBUG if arg else logging.INFO)
        return self

    def accept(self, arg=None):
        if arg:
            self._accept = arg
        else:
            self._accept = "application/json"
        return self

    def read_environmental_variables(self):
        if self._env is None:
            if 'ENV' in os.environ:
                self.env(os.environ['ENV'])
            else:
                self.env('test')

        if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
            self.debug()

        return self

    def configured_login(self, read_environment=False, create_config_file=False, config_dir=None, default_config_dirs=True):
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

        config_files = self.get_configfiles(config_dir = config_dir, default_config_dirs = default_config_dirs)

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

    def get_setting(self, name:str, description, write_settings = True) -> str:
        if not(name in self.settings):

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
                self._write_settings()
        return self.settings[name]

    @staticmethod
    def get_configfiles(config_dir = None, default_config_dirs = True) -> List[str]:
        current_script_dir = os.path.dirname(sys.argv[0])
        config_files = []
        if default_config_dirs:
            config_files = [
               os.path.join(os.path.expanduser("~"), "conf", "creds.properties"),
               os.path.join(current_script_dir, "..", "..", "..", "creds.properties"),
               os.path.join(current_script_dir, "..", "..", "..", "creds.sh"),
               os.path.join(current_script_dir, "creds.properties")
            ]

        if not config_dir is None:
            config_files.insert(0, os.path.join(config_dir, "creds.properties"))
        return config_files

    def _write_settings(self, config_dir = None):
        config_file = None
        config_files = self.get_configfiles(config_dir = config_dir)
        for file in self.get_configfiles():
            config_file = os.path.normpath(file)
            if os.access(os.path.dirname(config_file), os.W_OK):
                self.logger.debug("Found " + config_file)
                break
            else:
                self.logger.debug("Not writeable " + config_file)
                config_file = None

        if config_file:
            with open(str(config_file), "w") as f:
                f.write("# Automatically generated by " + __file__ + "\n")
                for key in self.settings:
                    if len(key.split(".")) == 1:
                        f.write(key + "=" + self.settings[key] + "\n")
                        f.write(key + "." + self.actualenv + "=" + self.settings[key] + "\n")
                    if len(key.split(".")) == 2:
                        f.write(key + "=" + self.settings[key] + "\n")
        else:
            print("(Configuration could not be saved since no file of %s is writable" % str(config_files))

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
                            split = value[len("system:"):].split(":", 1)
                            value = os.getenv(split[0])
                            if value is None:
                                value = split[1]
                        properties[key] = value
                    except Exception as e:
                        self.logger.error(l + ":" + str(e))
        return properties

    def _read_settings_from_properties(self, properties):
        for key, value in properties.items():
            split = key.split('.', 2)
            if len(split) == 1:
                self.settings[key.strip()] = value.strip('" \t')
        for key, value in properties.items():
            split = key.split('.', 2)
            if len(split) == 2:
                usedkey, e = split[0], split[1]
                if e == self.actualenv:
                    self.settings[usedkey.strip()] = value.strip('" \t')
                    self.logger.debug("%s %s %s %s", e, usedkey, key, value)
        return self.settings

    def anonymize_for_logging(self, settings_for_log):
        for key, vale in settings_for_log.items():
            if key in ["user", "pages_user", "parkpost_user"]:
                settings_for_log[key] = settings_for_log[key].split(":", 1)[0] + ":xxx"
            if key.endswith("secret"):
                settings_for_log[key] = "xxx"


    def command_line_client(self, description=None, read_environment=True, create_config_file=True, exclude_arguments=None):
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
        parent_args.add_argument('-v', "--version", action="store_true", help="show current version")
        if not "accept" in exclude_arguments:
            parent_args.add_argument('-a', "--accept", type=str, default=None, choices=self.accept_choices().keys())
        parent_args.add_argument('-e', "--env", type=str, default=None, choices={"test", "acc", "testa", "testb", "prod", "proda", "prodb", "prod_new", "dev", "test_new", "localhost"})
        parent_args.add_argument('-u', "--url", type=str, default=None, help="The URL of the API which this client communicates with. This is an alternative to --env")
        parent_args.add_argument('-c', "--createconfig", action='store_true', help="Create config")
        parent_args.add_argument('-d', "--debug", action='store_true', help="Switch on debug logging")
        parent_args.add_argument('-H', "--headers", action='store_true', help="Show relevant response headers")

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
        self.argument_parser = argparse.ArgumentParser(description=description,
                                                       parents=[parent_args],
                                                       epilog=NpoApiBase.EPILOG)
        return self

    def parse_args(self):
        args = self.argument_parser.parse_args()
        self.debug(args.debug)
        if "accept" in args and args.accept:
            self.accept(self.accept_choices().get(args.accept))
        else:
            self.accept()
        return args

    def get_response(self, req, url:str, ignore_not_found:bool = False, timeout:int = None) -> Optional[http.client.HTTPResponse]:
        """Error handling around urllib.request.urlopen

        :param ignore_not_found Whether status 404 should be logged as an error
        :param timeout Timeout in seconds

        """
        summary = "%s %s" % (req.method if hasattr(req, "method") else "'GET'" if not req.data else "'POST'", url)
        try:
            self.logger.debug("Executing %s", summary)
            response = urllib.request.urlopen(req, timeout=timeout)
            self.code = response.getcode()
            self.logger.debug("headers: "  + str(response.headers))
            if self.response_headers:
                self.logger.info("selector: %s " % (req.selector))
                for h in response.headers:
                    if h.startswith("X-NPO-warning"):
                        self.logger.warning("%s: %s" % (h, response.headers[h]))
                    elif h.startswith("X-NPO-"):
                        self.logger.info("%s: %s" % (h, response.headers[h]))
            else:
                 for h in response.headers:
                    if h.startswith("X-NPO-warning"):
                        self.logger.warning("%s" % (response.headers[h]))
            self.logger.debug("response code: " + str(response.getcode()))
            self.logger.debug("response headers: " + str(response.getheaders()))
            return response
        except urllib.error.URLError as ue:
            error_type = str(type(ue))
            self.logger.debug("headers: %s" % (str(ue.headers) if hasattr(ue, "headers") else "NONE"))
            if ignore_not_found and ue.code == 404:
                self.logger.debug('%s: %s: %s (%s)', url,  summary, ue.reason, error_type)
                self.code = 404
                return None
            if type(ue.reason) is str:
                self.logger.error('%s: %s: %s (%s)', url, summary, ue.reason, error_type)
                self.code = ue.code
            else:
                self.logger.error('%s: %s: %s %s (%s)', url, ue.reason.errno, summary, ue.reason.strerror, error_type)
                self.code = ue.reason.errno
            if hasattr(ue, "read"):
                self.logger.error("%s: %s", url, ue.read().decode("utf-8"))
            return None
        except urllib.error.HTTPError as he:
            self.code = he.code
            self.logger.error("%s: %s %s: %s\n%s", url, summary, he.code, he.msg, he.read().decode("utf-8"))
            return None

    def data_to_bytes(self, data, content_type:str = None) -> [bytearray, str]:
        """
        Given some object representing API data returns it as a bytearray and a content type.
        Recognized are pyxb bindings, a file name, or else a string.
        """
        if data:
            import pyxb
            import xml.dom.minidom
            if data is None:
                self.logger.warning("Data is none!")
            elif dataclasses.is_dataclass(data):
                serializer = XmlSerializer(config=SerializerConfig(pretty_print = False))
                content_type = "application/xml"
                data = serializer.render(data, ns_map=NS_MAP).encode("utf-8")
            elif isinstance(data, pyxb.binding.basis.complexTypeDefinition):
                self.logger.warning("pyxb is deprecated!")
                content_type = "application/xml"
                data = data.toxml("utf-8")
            elif isinstance(data, xml.dom.minidom.Document):
                data = data.toxml(encoding="utf-8")
            elif isinstance(data, str) and self.isfile(data):
                if content_type is None:
                    if data.endswith(".json"):
                        content_type = "application/json"
                    elif data.endswith(".xml"):
                        content_type = "application/xml"

                self.logger.debug("" + data + " is file, reading it in as " + content_type)
                with codecs.open(data, 'r', 'utf-8') as myfile:
                    data = myfile.read().encode('utf-8')
                    self.logger.debug("Found data " + data.decode("utf-8"))
            elif isinstance(data, str):
                if data == "-":
                    data = sys.stdin.read()
                    self.logger.debug("Slurping data from stdin -> " + data)
                content_type = None
                if data.startswith("{"):
                    content_type = "application/json"
                elif data.startswith("<"):
                    content_type = "application/xml"
                data = data.encode("utf-8")

        return data, content_type

    @staticmethod
    def isfile(string:str) -> bool:
        try:
            return os.path.isfile(string)
        except:
            return False

    def data_or_from_file(self, data: str) -> str:
        """"""
        if os.path.isfile(data):
            self.logger.debug("" + data + " is file, reading it in")
            with codecs.open(data, 'r', 'utf-8') as myfile:
                data = myfile.read()
                self.logger.debug("Found data " + data)
        else:
            if data == "-":
                data = sys.stdin.read()
            self.logger.debug("" + data + " is not a file")
        return data

    def to_object(self, data:str, validate=False, binding=Binding.PYXB) -> Optional[pyxb.binding.basis.complexTypeDefinition]:
        """Converts a string to a pyxb object and optionally validates it"""
        if data is None:
            return None
        if binding == binding.PYXB:
            self.logger.warning("pyxb is deprecated")
            if isinstance(data, pyxb.binding.basis.complexTypeDefinition):
                result = data
            else:
                from npoapi.xml import poms
                bytes, contenttype = self.data_to_bytes(data)
                result = poms.CreateFromDocument(bytes)

            if validate:
                result.validateBinding()
            return result
        else:
            if dataclasses.is_dataclass(data):
                result = data
            else:
                bytes, contenttype = self.data_to_bytes(data)
                result = XmlParser().from_bytes(bytes)
            if validate:
                self.logger.warning("Found out how to do that")
            return result


    def to_object_or_none(self, data:str, validate=False, binding=Binding.PYXB) -> object:
        import xml
        try:
            return self.to_object(data, validate, binding=binding)
        except xml.sax._exceptions.SAXParseException as e:
            self.logger.debug("Not xml")
            return None

    def exit_code(self) -> int:
        if self.code is None or 200 <= self.code < 300:
            return 0
        return self.code // 100

    def exit(self):
        sys.exit(self.exit_code())

    def pretty_xml(self, string: str) -> str:
        from xml.dom.minidom import parseString
        import xml.parsers.expat
        try:
            return parseString(string).toprettyxml(indent="  ")
        except xml.parsers.expat.ExpatError as e:
            self.logger.error(e)
            return string


    @abc.abstractmethod
    def info(self):
        return "ABSTRACT"
