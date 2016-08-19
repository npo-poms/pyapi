from npoapi.xml import media, mediaupdate, shared
from npoapi import MediaBackend

import pyxb
import logging

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
    def create_image(imageUrl: str):
        image_object = mediaupdate.image()
        image_object.type = shared.imageTypeEnum.PICTURE
        image_object.imageLocation = mediaupdate.imageLocationType()
        image_object.imageLocation.url = imageUrl
        image_object.highlighted = False
        return image_object

    @staticmethod
    def add_image(object: mediaupdate.mediaUpdateType, imageUrl: str):
        if not object.images:
            object.images = pyxb.BIND()

        image = MediaBackendUtil.create_image(imageUrl)
        object.images.append(image)
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
    def descendants(client: MediaBackend, mid:str, batch:int=200, target:list=None):
        if target is None:
            target = []
        target.extend(client.members(mid, batch=batch))
        target.extend(client.episodes(mid, batch=batch))

        for m in target:
            updateElement = m.getElementsByTagName("mediaUpdate")[0]
            if updateElement.getAttribute("xsi:type") == "groupUpdateType":
                MediaBackendUtil.descendants(client, updateElement.getAttribute("mid"), batch, target)

        return target






