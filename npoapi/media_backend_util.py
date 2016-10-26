import logging
import os

import pyxb
from xml.dom import minidom

from npoapi.media_backend import MediaBackend
from npoapi.xml import media, mediaupdate, poms


class MediaBackendUtil(object):
    logger = logging.getLogger("MediaBackendUtil")


    @staticmethod
    def main_title(object: mediaupdate.mediaUpdateType, string: str):
        result = MediaBackendUtil.title(object, media.textualTypeEnum.MAIN, string)
        if not result:
            MediaBackendUtil.logger.warn("Could not set main title because string was None")
        return result

    @staticmethod
    def main_description(object: mediaupdate.mediaUpdateType, string: str):
        return \
            MediaBackendUtil.description(object, media.textualTypeEnum.MAIN, string)


    @staticmethod
    def title(object: mediaupdate.mediaUpdateType, textualType, string: str):
        if string:
            title = mediaupdate.titleUpdateType(MediaBackendUtil.strip_tags(string))
            if type(textualType) is str:
                title.type = getattr(media.textualTypeEnum, textualType)
            else:
                title.type = textualType
            object.title.append(title)
            return title
        else:
            MediaBackendUtil.logger.debug("Not appending title because it is empty")
            return None

    @staticmethod
    def description(object: mediaupdate.mediaUpdateType, textualType, string: str):
        if string:
            description = mediaupdate.descriptionUpdateType(MediaBackendUtil.strip_tags(string))
            if type(textualType) is str:
                description.type = getattr(media.textualTypeEnum, textualType)
            else:
                description.type = textualType
            object.description.append(description)
            return description
        else:
            MediaBackendUtil.logger.debug("Not appending description because it is empty")
            return None


    @staticmethod
    def create_location(programUrl:str, **kwargs):
        # location_object = mediaupdate.locationUpdateType()
        location_object = mediaupdate.location()
        location_object.programUrl = programUrl
        return MediaBackendUtil.update_location(location_object, **kwargs)

    @staticmethod
    def update_location(location_object: mediaupdate.locationUpdateType,
                        avFileFormat=None, bitrate=None, height=None, width=None, aspectratio=None):
        programUrl = location_object.programUrl
        avAttributes = location_object.avAttributes
        if avAttributes is None:
            avAttributes = mediaupdate.avAtributeUpdateType()
            location_object.avAttributes = avAttributes

        if avFileFormat is None and avAttributes.avFileFormat is None:
            index = programUrl.rfind('.')
            ext = programUrl[index + 1:].upper()
            if hasattr(media.avFileFormatEnum, ext):
                avFileFormat = getattr(media.avFileFormatEnum, ext)
            else:
                avFileFormat = media.avFileFormatEnum.UNKNOWN

        if type(avFileFormat) is str:
            avFileFormat = getattr(media.avFileFormatEnum, avFileFormat)

        if avFileFormat:
            avAttributes.avFileFormat = avFileFormat
        if bitrate:
            location_object.avAttributes.bitrate = bitrate
        if height or width or aspectratio:
            location_object.avAttributes.videoAttributes = mediaupdate.videoAttributesUpdateType()
            location_object.avAttributes.videoAttributes.height = height
            location_object.avAttributes.videoAttributes.width = width
            location_object.avAttributes.videoAttributes.aspectRatio = getattr(media.aspectRatioEnum, aspectratio, None)

        return location_object


    @staticmethod
    def add_location(object: mediaupdate.mediaUpdateType, programUrl:str, **kwargs):
        if not object.locations:
            object.locations = pyxb.BIND()

        location = MediaBackendUtil.create_location(programUrl, **kwargs)
        object.locations.append(location)
        return location

    @staticmethod
    def get_location(object: mediaupdate.mediaUpdateType, programUrl:str) -> mediaupdate.locationUpdateType:
        if not object.locations:
            return None
        for loc in object.locations.location:
            if str(loc.programUrl) is str(programUrl):
                return loc
        return loc

    @staticmethod
    def add_or_update_location(object: mediaupdate.mediaUpdateType, programUrl:str, **kwargs) -> mediaupdate.locationUpdateType:
        loc = MediaBackendUtil.get_location(object, programUrl)
        if loc:
            logging.debug("Found existing %s for %s", loc, programUrl)
            return MediaBackendUtil.update_location(loc, **kwargs)
        else:
            return MediaBackendUtil.add_location(object, programUrl, **kwargs)


    @staticmethod
    def create_image_from_file(image, **kwargs):
        if os.path.isfile(image):
            with open(image, "rb") as image_file:
                image_object = mediaupdate.image()
                image_object.imageData = mediaupdate.imageDataType()
                image_object.imageData.data = image_file.read()
                MediaBackendUtil.set_image_fields(image_object, **kwargs)
                return image_object
        return None

    @staticmethod
    def create_image_from_url(imageUrl: str, **kwargs):
        image_object = mediaupdate.image()

        if imageUrl.startswith("urn:"):
            image_object.urn = imageUrl
        else:
            image_object.imageLocation = mediaupdate.imageLocationType()
            image_object.imageLocation.url = imageUrl
        MediaBackendUtil.set_image_fields(image_object, **kwargs)
        return image_object

    @staticmethod
    def set_image_fields(image_object, image_type="PICTURE", title=None, description=None, highlighted=False):
        image_object.type = image_type
        #shared.imageTypeEnum.PICTURE
        image_object.highlighted = highlighted
        if title:
            image_object.title = MediaBackendUtil.strip_tags(title)
        if description:
            image_object.description = MediaBackendUtil.strip_tags(description)

    @staticmethod
    def add_image(object: mediaupdate.mediaUpdateType, image: str, **kwargs):
        if not object.images:
            object.images = pyxb.BIND()

        new_image = MediaBackendUtil.create_image(image, **kwargs)
        object.images.append(new_image)
        return image


    @staticmethod
    def create_image(image: str, **kwargs):
        if type(image) == str and os.path.isfile(image):
            return MediaBackendUtil.create_image_from_file(image, **kwargs)
        else:
            return MediaBackendUtil.create_image_from_url(image, **kwargs)


    @staticmethod
    def add_or_update_location(object: mediaupdate.mediaUpdateType, programUrl: str,
                               **kwargs) -> mediaupdate.locationUpdateType:
        loc = MediaBackendUtil.get_location(object, programUrl)
        if loc:
            logging.debug("Found existing %s for %s", loc, programUrl)
            return MediaBackendUtil.update_location(loc, **kwargs)
        else:
            return MediaBackendUtil.add_location(object, programUrl, **kwargs)

    @staticmethod
    def member_of(object: mediaupdate.mediaUpdateType, group:str, position:int=None):
        memberOf = mediaupdate.memberRefUpdateType(group)
        memberOf.highlighted = False
        if position is not None:
            memberOf.position = position
        object.memberOf.append(memberOf)

    @staticmethod
    def descendants(client: MediaBackend, mid: str, batch: int = 200, target: list = None, log_progress: bool = False, log_indent=""):
        """Returns a list of dom"""

        if target is None:
            target = []
        new_targets = []
        if log_progress:
            MediaBackendUtil.logger.info("%sGetting members of %s", log_indent, mid)
        new_targets.extend(client.members(mid, batch=batch, log_progress=log_progress, log_indent=log_indent))
        if log_progress:
            MediaBackendUtil.logger.info("%sGetting episodes of %s", log_indent, mid)
        new_targets.extend(client.episodes(mid, batch=batch, log_progress=log_progress, log_indent=log_indent))
        target.extend(new_targets)
        for m in new_targets:
            updateElement = m.getElementsByTagName("mediaUpdate")[0]
            if updateElement.getAttribute("xsi:type") == "groupUpdateType":
                group_mid = updateElement.getAttribute("mid")
                if log_progress:
                    MediaBackendUtil.logger.info("%sThis is a group %s. Recursing", log_indent, group_mid)
                MediaBackendUtil.descendants(client, group_mid, batch, target, log_progress=log_progress, log_indent=log_indent + "   ")

        return target


    @staticmethod
    def iterate_objects(members):
        if type(members) == str:
            members = minidom.parseString(members)
        if type(members) == minidom.Document:
            members = members.getElementsByTagName('item')

        result = map(lambda m:
                     poms.CreateFromDOM(m.getElementsByTagName("mediaUpdate")[0], mediaupdate.Namespace),
                      members)
        return result

    @staticmethod
    def parse(duration_in_ms: int):
        """Converts millis to hours, minutes, seconds, millis"""
        millis = duration_in_ms % 1000
        seconds = duration_in_ms / 1000
        hours = seconds // 3600
        seconds -= hours * 3600
        minutes = seconds // 60
        seconds -= minutes * 60
        return (hours, minutes, seconds, millis)

    @staticmethod
    def un_parse(hours, minutes, seconds, millis=0):
        return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis

    @staticmethod
    def format_duration(duration_in_ms: int):
        """ Format duration as a ISO_8601"""
        (hours, minutes, seconds, millis) = MediaBackendUtil.parse(duration_in_ms)
        if hours == 0 and minutes == 0 and millis == 0:
            return "P0DT%dS" % seconds
        else:
            return "P0DT%dH%dM%d.%03dS" % (hours, minutes, seconds, millis)



    def strip_tags(html:str) -> str:
        s = MLStripper()
        s.feed("<html>" + html + "</html>")
        return s.get_data()


from html.parser import HTMLParser
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)
