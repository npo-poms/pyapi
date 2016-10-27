import abc
import argparse
import codecs
import copy
import logging
import os
import sys
import urllib.request

import pyxb

import npoapi


def declare_namespaces():
    import pyxb.utils.domutils
    from npoapi.xml import mediaupdate, pageupdate, page, media, shared, api

    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(mediaupdate.Namespace)
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pageupdate.Namespace, 'pu')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(page.Namespace, 'pages')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(media.Namespace, 'media')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(shared.Namespace, 'shared')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(api.Namespace, 'api')


declare_namespaces()


class NpoApiBase:
    """Base class for all api client (both backend and frontend)"""
    __metaclass__ = abc.ABCMeta
    EPILOG = """
    DEBUG=true and ENV=<dev|test|prod> environment variables are recognized.
    Credentials are read from a config file. If such a file does not exist it will offer to create one.
    """

    def __init__(self, env: str = None, debug: bool = False, accept: str = None):
        """
        Initializes logging, env-settings, and default accept headers.
        """
        self.force_create_config = False
        self.code = None

        logging.basicConfig(format='%(levelname)s %(message)s')
        self.logger = logging.getLogger("Npo")
        self.debug(debug)
        self._env = env
        self.env(env)
        self.accept(accept)

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

    def configured_login(self, read_environment=False, create_config_file=False, config_dir=None):
        """
        Logs in using configuration file. Considered using json (no comments-> unusable) or configparser (nearly properties, but headings are required..)
        So, now it simply parses the file itself.
        :param create_config_file: If there is no existing config file, offer to create one
        :param read_environment: If this is set to true, shel environment variables like DEBUG and ENV will be recognized
        """
        if read_environment:
            self.read_environmental_variables()

        config_files = [
            os.path.join(os.path.expanduser("~"), "conf", "creds.properties"),
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "creds.properties"),
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "creds.sh"),
            os.path.join(os.path.dirname(__file__), "creds.properties")]

        if not config_dir is None:
            config_files.insert(0, os.path.join(config_dir, "creds.properties"))

        config_file = None
        for file in config_files:
            if os.path.isfile(file):
                config_file = os.path.normpath(file)
                break
            else:
                self.logger.debug("not a file " + file)

        settings = {}
        if config_file:
            self.logger.debug("Reading " + str(config_file) + " for env " + self.actualenv)
            properties = self.read_properties_file(config_file)
            self.read_settings_from_properties(properties, settings)

        if not config_file and create_config_file:
            print("No configuration file found. Now creating.")
            self.force_create_config = True

        if self.force_create_config:
            self.create_config(settings)
            config_file = None
            for file in config_files:
                config_file = os.path.normpath(file)
                if os.access(os.path.dirname(config_file), os.W_OK):
                    self.logger.debug("Found " + config_file)
                    break
                else:
                    self.logger.debug("Not writeable " + config_file)
                    config_file = None

            if config_file:
                with open(str(config_file), "w") as f:
                    f.write("# Automaticly generated by " + __file__ + "\n")
                    for key in settings:
                        if len(key.split(".")) == 1:
                            f.write(key + "=" + settings[key] + "\n")
                            f.write(key + "." + self.actualenv + "=" + settings[key] + "\n")
                        if len(key.split(".")) == 2:
                            f.write(key + "=" + settings[key] + "\n")
            else:
                print("(Configuration could not be saved since no file of %s is writable" % str(config_files))

        if self.logger.isEnabledFor(logging.DEBUG):
            settings_for_log = copy.copy(settings)
            self.anonymize_for_logging(settings_for_log)
            self.logger.debug("settings" + str(settings_for_log))

        self.logger.debug("Reading settings")
        self.read_settings(settings)

        return self

    def read_properties_file(self, config_file, properties=None):
        if properties is None:
            properties = {}
        with open(config_file, "r") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith("#"):
                    key, value = l.split("=", 2)
                    properties[key] = value.strip('" \t')
        return properties

    def read_settings_from_properties(self, properties, settings=None):
        if settings is None:
            settings = {}
        for key, value in properties.items():
            split = key.split('.', 2)
            if len(split) == 1:
                settings[key.strip().lower()] = value.strip('" \t')
        for key, value in properties.items():
            split = key.split('.', 2)
            if len(split) == 2:
                usedkey, e = split[0], split[1]
                if e == self.actualenv:
                    settings[usedkey.strip().lower()] = value.strip('" \t')
                    self.logger.debug("%s %s %s %s", e, usedkey, key, value)
        return settings

    def anonymize_for_logging(self, settings_for_log):
        if 'secret' in settings_for_log:
            settings_for_log['secret'] = "xxx"
        for key, vale in settings_for_log.items():
            if key.endswith("user"):
                settings_for_log[key] = settings_for_log[key].split(":", 1)[0] + ":xxx"
        return

    @abc.abstractmethod
    def create_config(self, settings):
        """

        """

        return self

    @abc.abstractmethod
    def read_settings(self, settings):
        """
        """
        return

    def command_line_client(self, description=None, read_environment=True, create_config_file=True, exclude_arguments=None):
        self.common_arguments(description=description, exclude_arguments=exclude_arguments)
        return self.configured_login(read_environment=read_environment, create_config_file=create_config_file)

    def add_argument(self, *args, **kwargs):
        self.argument_parser.add_argument(*args, **kwargs)

    def accept_choices(self):
        return {"json": "application/json", "xml": "application/xml"}

    def common_arguments(self, description=None, exclude_arguments=None):
        if exclude_arguments is None:
            exclude_arguments = {}
        parent_args = argparse.ArgumentParser(add_help=False)
        parent_args.add_argument('-v', "--version", action="store_true", help="show current version")
        if not "accept" in exclude_arguments:
            parent_args.add_argument('-a', "--accept", type=str, default=None, choices=self.accept_choices().keys())
        parent_args.add_argument('-e', "--env", type=str, default=None, choices={"test", "prod", "dev", "localhost"})
        parent_args.add_argument('-u', "--url", type=str, default=None)
        parent_args.add_argument('-c', "--createconfig", action='store_true', help="Create config")
        parent_args.add_argument('-d', "--debug", action='store_true', help="Switch on debug logging")
        filtered_argv = []
        i = 0
        while i < len(sys.argv):
            a = sys.argv[i]
            if a in ["-d", "--debug", "-c", "--createconfig", "-v", "--version"]:
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
        if pargs.url:
            self.env(pargs.url)
        if pargs.version:
            print(npoapi.__version__)
            exit(0)
        self.force_create_config = pargs.createconfig
        self.argument_parser = argparse.ArgumentParser(description=description,
                                                       parents=[parent_args],
                                                       epilog=NpoApiBase.EPILOG)

    def parse_args(self):
        args = self.argument_parser.parse_args()
        self.debug(args.debug)
        if "accept" in args and args.accept:
            self.accept(self.accept_choices().get(args.accept))
        return args

    def get_response(self, req, url, ignore_not_found=False, timeout=None):
        """Error handling around urllib.request.urlopen"""
        summary = "%s %s" % (req.method if hasattr(req, "method") else "'GET'" if not req.data else "'POST'", url)
        try:
            self.logger.debug("Executing %s", summary)
            response = urllib.request.urlopen(req, timeout=timeout)
            self.code = response.getcode()
            self.logger.debug("response code: " + str(response.getcode()))
            self.logger.debug("response headers: " + str(response.getheaders()))
            return response
        except urllib.error.URLError as ue:
            error_type = str(type(ue))

            if ignore_not_found and ue.code == 404:
                self.logger.debug('%s: %s (%s)', summary, ue.reason, error_type)
                self.code = 404
                return None
            if type(ue.reason) is str:
                self.logger.error('%s: %s (%s)', summary, ue.reason, error_type)
                self.code = ue.code
            else:
                self.logger.error('%s: %s %s (%s)', ue.reason.errno, summary, ue.reason.strerror, error_type)
                self.code = ue.reason.errno
            if hasattr(ue, "read"):
                self.logger.error("%s", ue.read().decode("utf-8"))
            return None
        except urllib.error.HTTPError as he:
            self.code = he.code
            self.logger.error("%s %s: %s\n%s", summary, he.code, he.msg, he.read().decode("utf-8"))
            return None

    def data_to_bytes(self, data, content_type=None):
        """
        Gives some object representing API data returns it as a string.
        Recognized are pyxb bindings, a files name, or else a string.
        """
        if data:
            import pyxb
            import xml.dom.minidom
            if isinstance(data, pyxb.binding.basis.complexTypeDefinition):
                content_type = "application/xml"
                data = data.toxml()
            elif isinstance(data, xml.dom.minidom.Document):
                data = data.toxml().encode("utf-8")
            elif os.path.isfile(data):
                if content_type is None:
                    if data.endswith(".json"):
                        content_type = "application/json"
                    elif data.endswith(".xml"):
                        content_type = "application/xml"

                self.logger.debug("" + data + " is file, reading it in as " + content_type)
                with codecs.open(data, 'r', 'utf-8') as myfile:
                    data = myfile.read()
                    self.logger.debug("Found data " + data)

        return data, content_type

    def data_or_from_file(self, data: str):
        """"""
        if os.path.isfile(data):
            self.logger.debug("" + data + " is file, reading it in")
            with codecs.open(data, 'r', 'utf-8') as myfile:
                data = myfile.read()
                self.logger.debug("Found data " + data)
        else:
            self.logger.debug("" + data + " is not a file")
        return data

    def to_object(self, data, validate=False) -> pyxb.binding.basis.complexTypeDefinition:
        """Converts a string to a pyxb object and optionally validates it"""
        if data is None:
            return None
        object = None
        if isinstance(data, pyxb.binding.basis.complexTypeDefinition):
            object = data
        else:
            from npoapi.xml import poms
            object = poms.CreateFromDocument(self.data_to_bytes(data)[0])

        if validate:
            object.validateBinding()
        return object

    def to_object_or_none(self, data, validate=False) -> pyxb.binding.basis.complexTypeDefinition:
        import xml
        try:
            self.to_object(data, validate)
        except xml.sax._exceptions.SAXParseException as e:
            self.logger.debug("Not xml")
            return None

    def exit_code(self):
        if self.code is None or 200 <= self.code < 300:
            return 0
        return self.code // 100

    def exit(self):
        sys.exit(self.exit_code())

    @abc.abstractmethod
    def info(self):
        return "ABSTRACT"
