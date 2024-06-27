import codecs
import logging
import os
import time
import urllib.parse
from datetime import datetime
from typing import Dict, Optional, Union
from xml.dom import minidom

import lxml
from typing_extensions import override
from xsdata.models.datatype import XmlDateTime

from npoapi import data
from npoapi.base import DEFAULT_BINDING
from npoapi.basic_backend import BasicBackend
from npoapi.data import (
    BaseMediaType,
    LocationUpdateType,
    MediaUpdateType,
    Prediction,
    PredictionUpdateType,
    StreamingStatus,
)
from npoapi.xml import media, mediaupdate, poms
from npoapi.xml.media import baseMediaType, streamingStatus
from npoapi.xml.mediaupdate import mediaUpdateType


class MediaBackend(BasicBackend):
    """Client for NPO Backend API"""

    __author__ = "Michiel Meeuwissen"

    def __init__(self, env: str = None, email: str = None, debug: bool = False, accept: str = None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__("Media Backend", env, email, debug, accept)
        self.parkpost_authorization = None

    def env(self, e: str):
        super().env(e)
        if e == "prod":
            self.url = "https://api.poms.omroep.nl/"
        elif e == None or e == "test":
            self.url = "https://api-test.poms.omroep.nl/"
        elif e == "acc":
            self.url = "https://api-acc.poms.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8071/rs/"
        else:
            self.url = e
        return self

    def get(self, mid: str, ignore_not_found=False, accept="application/xml") -> str:
        """Returns XML or json -representation of a mediaobject (as a string)"""
        return self.get_from(
            "media/media/" + urllib.parse.quote(mid, safe=""), ignore_not_found=ignore_not_found, accept=accept
        )[0]

    def get_full(self, mid: str, ignore_not_found=False, accept="application/xml") -> str:
        """Returns XML-representation of a mediaobject (as a string)"""
        return self.get_from(
            "media/media/" + urllib.parse.quote(mid, safe="") + "/full",
            ignore_not_found=ignore_not_found,
            accept=accept,
        )[0]

    def get_object(
        self, mid: str, ignore_not_found=False, binding=DEFAULT_BINDING
    ) -> Union[mediaUpdateType, MediaUpdateType]:
        """Returns xsdata/pyxb-representation of a mediaobject"""
        return self.to_object(self.get(mid, ignore_not_found), validate=False, binding=binding)

    def get_full_object(
        self, mid: str, ignore_not_found=False, binding=DEFAULT_BINDING
    ) -> Union[baseMediaType, BaseMediaType]:
        """Returns xsdata/pyxb-representation of a mediaobject"""
        return self.to_object(self.get_full(mid, ignore_not_found), validate=False, binding=binding)

    def exists(self, mid: str):
        return self.get_from("media/exists/" + urllib.parse.quote(mid, safe=""), accept="")[0] == "true"

    def streaming_status(self, mid: str, binding=DEFAULT_BINDING) -> Union[streamingStatus, StreamingStatus]:
        return self.to_object(
            self.get_from("media/streamingstatus/" + urllib.parse.quote(mid, safe=""))[0], binding=binding
        )

    def post(
        self,
        update,
        lookupcrid=True,
        raw=False,
        steal_crids="IF_DELETED",
        validate_input=False,
        client_validate=True,
        sub=None,
        mid=None,
        binding=DEFAULT_BINDING,
    ) -> Optional[str]:
        if not raw:
            update = self.to_object(update, validate=client_validate, binding=binding)
        target = "media/media/"
        if mid is not None and len(mid) > 0:
            target = target + urllib.parse.quote(mid, safe="") + "/"
        if sub is not None and len(sub) > 0:
            target = target + urllib.parse.quote(sub, safe="") + "/"

        return self.post_to(
            target,
            update,
            accept="text/plain",
            errors=self.get_errors(),
            lookupcrid=lookupcrid,
            stealcrids=steal_crids,
            validateInput=str(validate_input).lower(),
        )[0]

    def post_prediction(self, mid, update: Prediction) -> Optional[str]:
        target = "media/media/%s/predictions/%s" % (mid, update.value)

        return self.post_to(target, update, accept="application/xml", errors=self.get_errors())[0]

    def delete(self, mid: str) -> Optional[str]:
        """"""
        return self.delete_from("media/media/" + urllib.parse.quote(mid, safe=""))[0]

    def _parkpost_authentication(self):
        if not (self.parkpost_authorization):
            self.parkpost_authorization = self._basic_authentication("parkpost_user", "Your NPO backend parkpost")

    def parkpost(self, xml) -> Optional[str]:
        self._parkpost_authentication()
        url = self.url + "parkpost/promo"
        req = urllib.request.Request(url, data=self.xml_to_bytes(xml))
        return self._request(req, url, accept="application/xml", authorization=self.parkpost_authorization)[0]

    def find(
        self, form, writable=False, raw=False, validate_input=False, client_validate=True, binding=DEFAULT_BINDING
    ) -> Optional[str]:
        if not raw:
            form = self.to_object(form, validate=client_validate, binding=binding)
        return self.post_to(
            "media/find", form, accept="application/xml", writable=writable, validateInput=str(validate_input).lower()
        )[0]

    def subtitles(self, mid: str, language=None, type="CAPTION") -> Optional[str]:
        path = mid
        if language:
            path += "/" + language + "/" + type
        return self.get_from("media/subtitles/" + path, accept="application/xml")[0]

    def members(self, mid: str, **kwargs) -> list:
        """return a list of all members of a group. As minidom  XML objects, wrapped
        in 'items', so you can see the position"""
        return self.members_or_episodes(mid, "members", **kwargs)

    def episodes(self, mid, **kwargs) -> list:
        """return a list of all episodes of a group. As minidom XML objects, wrapped
        in 'items', so you can see the position"""
        return self.members_or_episodes(mid, "episodes", **kwargs)

    def delete_member(self, mid, owner_mid) -> Optional[str]:
        path = "media/media/" + urllib.parse.quote(mid, safe="") + "/memberOf/" + urllib.parse.quote(owner_mid, safe="")
        return self.delete_from(path)[0]

    def add_member(self, mid, owner_mid, position=None, highlighted=False) -> Optional[str]:
        memberOf = mediaupdate.memberRef(owner_mid)
        memberOf.position = position
        memberOf.highlighted = highlighted
        path = "media/media/" + urllib.parse.quote(mid, safe="") + "/memberOf/"
        return self.post_to(path, memberOf, accept="application/xml")[0]

    # method to implement both members and episodes calls.
    def members_or_episodes(
        self,
        mid: str,
        what: str,
        limit: int = None,
        batch: int = 20,
        log_progress=False,
        log_indent="",
        full=False,
        follow_merges=True,
        deletes=False,
        raw=False,
        accept="application/xml",
    ) -> Optional[Union[list, str]]:
        """Returns a list of minidom objects"""
        self._creds()
        self.logger.log(logging.INFO if log_progress else logging.DEBUG, "loading %s of %s", what, mid)
        result = []
        offset = 0
        b = min(batch, limit) if limit else batch
        sub = "group" if what == "episodes" else "media"
        w = what + "/full" if full else what
        while True:
            url = (
                self.url
                + "media/"
                + sub
                + "/"
                + urllib.parse.quote(mid, safe="")
                + "/"
                + w
                + "?max="
                + str(b)
                + "&offset="
                + str(offset)
            )
            if deletes:
                url = url + "&deletes=true"
            if not follow_merges:
                url = url + "&followMerges=false"

            if accept == "application/json" and not raw:
                self.logger("Cannot parse json, so raw is forced")
                raw = True

            bytes: bytes = self._get(url, accept=accept)
            if bytes:
                if raw:
                    return bytes.decode("utf-8")
                else:
                    xml = minidom.parseString(bytes)
                    items = xml.getElementsByTagNameNS("*", "item")
                    # result.extend(map(lambda i: poms.CreateFromDOM(i, default_namespace=mediaupdate.Namespace), items))
                    result.extend(items)
                    total = xml.childNodes[0].getAttribute("totalCount")
                    if len(items) == 0 or (limit and len(result) >= limit):
                        break
                    if len(items) != len(result):
                        self.logger.log(
                            logging.INFO if log_progress else logging.DEBUG,
                            "%s%s of %s: %s/%s (+%s)",
                            log_indent,
                            what,
                            mid,
                            len(result),
                            total,
                            len(items),
                        )
                    else:
                        self.logger.log(
                            logging.INFO if log_progress else logging.DEBUG,
                            "%s%s of %s: %s/%s",
                            log_indent,
                            what,
                            mid,
                            len(result),
                            total,
                        )
                    offset += b
                    # print xml.childNodes[0].toxml('utf-8')
                    self.logger.debug(str(len(result)) + "/" + total + (("/" + str(limit)) if limit else ""))
            else:
                self.logger.debug("None returned from %s", url)
                time.sleep(2)

        return result

    def post_location(
        self,
        mid: str,
        programUrl,
        duration: str = None,
        bitrate: int = None,
        height: int = None,
        width: int = None,
        aspectRatio: str = None,
        format: str = None,
        publishStart=None,
        publishStop=None,
    ) -> str:
        if os.path.isfile(programUrl):
            self.logger.debug(programUrl + " seems to be a local file")
            with codecs.open(programUrl, "r", "utf-8") as myfile:
                xml = myfile.read()
        else:
            if not format:
                format = self.guess_format(programUrl)

            xml = (
                "<location xmlns='urn:vpro:media:update:2009'"
                + self.date_attr("publishStart", publishStart)
                + self.date_attr("publishStop", publishStop)
                + ">"
                + "  <programUrl>"
                + programUrl
                + "</programUrl>"
                + "   <avAttributes>"
            )
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
        return self.post_to("media/media/" + mid + "/location", xml, accept="text/plain")[0]

    def date_attr(self, name: str, datetime):
        if datetime:
            return " " + name + "='" + self.date_attr_value(datetime) + "'"
        else:
            return ""

    def add_image(self, mid: str, image) -> str:
        return self.post_to("media/media/" + mid + "/image", image, accept="text/plain")[0]

    def itemize(self, mid: str, itemize) -> str:
        iobject = self.to_object(itemize)
        if mid is None:
            mid = iobject.mid
        return self.post_to("media/media/" + mid + "/itemize", iobject, accept="application/xml")[0]

    def add_location(self, mid: str, location) -> str:
        return self.post_to("media/media/" + mid + "/location", location, accept="text/plain")[0]

    def set_location(
        self,
        mid: str,
        location: Union[str, int],
        publishStop: Union[str, datetime] = None,
        publishStart: Union[str, datetime] = None,
        programUrl: str = None,
        only_if_exists: bool = False,
    ) -> Optional[str]:
        locations = data.poms.from_bytes(self.get_locations(mid))
        location_object = None
        for l in locations.otherElement:
            if type(location) == int or (type(location) == str and location.isdigit()):
                # given location is given as digit
                if (l.urn is not None and str(l.urn).endswith(":" + str(location))) and (
                    programUrl is None or str(l.programUrl) == programUrl
                ):
                    location_object = l
                    break
            elif str(l.urn).startswith("urn:vpro:media:location:"):
                # given location is given as urn
                if (str(l.urn) == location) and (programUrl is None or str(l.programUrl) == programUrl):
                    location_object = l
                    break

            # given location is given as programUrl
            if str(l.programUrl) == location:
                location_object = l
                break

        if location_object is None:
            if only_if_exists:
                return None
            # location_object = mediaupdate.locationUpdateType()
            location_object = data.poms.from_string("""<location xmlns="urn:vpro:media:update:2009">
<programUrl>http://www.vpro.nl/123</programUrl>
<avAttributes>
<avFileFormat>MP4</avFileFormat>
</avAttributes>
</location>""")
            if programUrl is not None:
                location_object.programUrl = programUrl
            elif not isinstance(location, int) and not location.isdigit():
                location_object.programUrl = location
            else:
                return None
        location_object.avAttributes.avFileFormat = self.guess_format(location_object.programUrl)

        self.logger.debug("no match for %s. Created location." % location)

        self.logger.debug("Processing %s" % location_object)

        if publishStop:
            location_object.publishStop = data.poms.to_xml_data_time(publishStop)
        if publishStart:
            location_object.publishStart = data.poms.to_xml_date_time(publishStart)

        location_xml = data.poms.to_xml(location_object)
        self.logger.debug("Found " + location_xml)
        return self.post_to("media/media/" + mid + "/location", location_xml, accept="text/plain")[0]

    def get_locations(self, mid: str) -> bytes:
        return self.get_sub(mid, "locations")

    def get_images(self, mid: str) -> bytes:
        return self.get_sub(mid, "images")

    def get_sub(self, mid: str, sub: str, deletes=False, follow_merges=True, accept=None) -> bytes:
        self._creds()
        effective_sub = "" if sub is None or sub == "" else "/" + sub
        url = self.url + "media/media/" + urllib.parse.quote(mid, safe="") + effective_sub
        sep = "?"
        if deletes:
            url = url + sep + "deletes=true"
            sep = "&"
        if not follow_merges:
            url = url + sep + "followMerges=false"
        return self._get(url, accept=accept)

    @staticmethod
    def guess_format(url):
        if str(url).endswith(".mp4"):
            return media.avFileFormatEnum.MP4
        elif str(url).endswith(".mp3"):
            return media.avFileFormatEnum.MP3
        else:
            return media.avFileFormatEnum.UNKNOWN

    def upload_audio(self, mid: str, file: str, **kwargs):
        if not (file.endswith(".mp3")):
            return "not an mp3 " + file
        return self.upload(mid, file, **kwargs)

    def upload(self, mid: str, file: str, content_type: None, **kwargs):
        parseable_response = True
        post_fix = ""
        encryption = kwargs.get("encryption", None)
        priority = kwargs.get("priority", None)
        transcode = kwargs.get("transcode", True)
        if content_type is None:
            if file.endswith(".mp3"):
                content_type = "audio/mp3"
            elif file.endswith(".mp4"):
                content_type = "video/mp4"
            else:
                return "not supported " + file
        if content_type.startswith("video/"):
            if transcode:
                post_fix = "/%s/%s" % (
                    "NONE" if encryption is None else encryption,
                    "NORMAL" if priority is None else priority,
                )
                parseable_response = False
        if content_type.startswith("audio/"):
            if encryption is not None or priority is not None:
                raise "encryption and priority only for video"
            if not transcode:
                raise "audio is always implicitly transcoded to mp3"

        path = "media/upload/%s%s" % (urllib.parse.quote(mid, safe=""), post_fix)

        with open(file, "rb") as f:
            response = self.post_bytes_to_response(
                path, f, content_type=content_type, content_length=os.stat(file).st_size, accept="", **kwargs
            )
            self.logger.info("Response: %s" % str(response))
            if response is None:
                self.logger.error("No response")
                return "no response"
            else:
                result = self.write_response(response, buffer_size=1, capture=True)
                if parseable_response:
                    try:
                        from npoapi.data import poms

                        return poms.from_string(result)
                    except Exception as e:
                        self.logger.error("Error parsing for %s '%s': %s" % (mid, result, e))
                        return None
                else:
                    return result

    @override
    def accept_choices(self) -> Dict[str, str]:
        return {"xml": "application/xml", "json": "application/json"}

    @override
    def __str__(self) -> str:
        return super().__str__() + " (media)"
