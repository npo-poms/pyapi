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
        MediaBackendUtil.title(object, media.textualTypeEnum.MAIN, string)

    @staticmethod
    def main_description(object: mediaupdate.mediaUpdateType, string: str):
        MediaBackendUtil.description(object, media.textualTypeEnum.MAIN, string)


    @staticmethod
    def title(object: mediaupdate.mediaUpdateType, textualType, string: str):
        title = mediaupdate.titleUpdateType(string)
        if type(textualType) is str:
            title.type = getattr(media.textualTypeEnum, textualType)
        else:
            title.type = textualType
        object.title.append(title)

    @staticmethod
    def description(object: mediaupdate.mediaUpdateType, textualType, string: str):
        description = mediaupdate.descriptionUpdateType(string)
        if type(textualType) is str:
            description.type = getattr(media.textualTypeEnum, textualType)
        else:
            description.type = textualType
        object.description.append(description)

    @staticmethod
    def create_location(programUrl:str, **kwargs):
        # location_object = mediaupdate.locationUpdateType()
        location_object = mediaupdate.location()
        location_object.programUrl = programUrl
        return MediaBackendUtil.update_location(location_object, **kwargs)

    @staticmethod
    def update_location(location_object: mediaupdate.locationUpdateType, avFileFormat=None, bitrate=None, height=None, width=None, aspectratio=None):
        programUrl = location_object.programUrl
        avAttributes = location_object.avAttributes
        if avAttributes is None:
            avAttributes = mediaupdate.avAtributeUpdateType()
            location_object.avAttributes = avAttributes

        if avFileFormat is None and avAttributes.avFileFormat is None:
            index = programUrl.rfind('.')
            avFileFormat = getattr(media.avFileFormatEnum, programUrl[index + 1:].upper())
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
    def create_image(imageUrl: str, **kwargs):
        image_object = mediaupdate.image()

        image_object.imageLocation = mediaupdate.imageLocationType()
        image_object.imageLocation.url = imageUrl
        MediaBackendUtil.set_image_fields(image_object, **kwargs)
        return image_object

    @staticmethod
    def set_image_fields(image_object, image_type="PICTURE", title=None, description=None):
        image_object.type = image_type
        #shared.imageTypeEnum.PICTURE
        image_object.highlighted = False
        if title:
            image_object.title = title
        if description:
            image_object.description = description

    @staticmethod
    def add_image(object: mediaupdate.mediaUpdateType, image: str, **kwargs):
        if not object.images:
            object.images = pyxb.BIND()

        if type(image) == str and os.path.isfile(image):
            new_image = MediaBackendUtil.create_image_from_file(image, **kwargs)
        else:
            new_image = MediaBackendUtil.create_image(image, **kwargs)
        object.images.append(new_image)
        return image

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
    def descendants(client: MediaBackend, mid: str, batch: int = 200, target: list = None):
        """Returns a list of dom"""
        if target is None:
            target = []
        target.extend(client.members(mid, batch=batch))
        target.extend(client.episodes(mid, batch=batch))

        for m in target:
            updateElement = m.getElementsByTagName("mediaUpdate")[0]
            if updateElement.getAttribute("xsi:type") == "groupUpdateType":
                MediaBackendUtil.descendants(client, updateElement.getAttribute("mid"), batch, target)

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
    def format_duration(duration_in_ms: int):
        """ Format duration as a ISO_8601"""
        (hours, minutes, seconds, millis) = MediaBackendUtil.parse(duration_in_ms)
        if hours == 0 and minutes == 0 and millis == 0:
            return "P0DT%dS" % seconds
        else:
            return "P0DT%dH%dM%d.%03dS" % (hours, minutes, seconds, millis)




