from npoapi.xml import media, mediaupdate
import pyxb

class MediaBackendUtil(object):

    @staticmethod
    def main_title(object: mediaupdate.mediaUpdateType, string: str):
        MediaBackendUtil.title(object, media.textualTypeEnum.MAIN, string)


    @staticmethod
    def title(object: mediaupdate.mediaUpdateType, textualType, string: str):
        title = mediaupdate.titleUpdateType(string)
        if type(textualType) is str:
            title.type = getattr(media.textualTypeEnum, textualType)
        else:
            title.type = textualType
        object.title.append(title)

    @staticmethod
    def create_location(programUrl:str, avType = None):
        # location_object = mediaupdate.locationUpdateType()
        location_object = mediaupdate.location()
        location_object.programUrl = programUrl
        avAttributes = mediaupdate.avAtributeUpdateType()
        if avType is None:
            index = programUrl.rfind('.')
            avType = getattr(media.avFileFormatEnum, programUrl[index + 1:].upper())
        if type(avType) is str:
            getattr(media.avFileFormatEnum, avType)

        avAttributes.avFileFormat = avType
        location_object.avAttributes = avAttributes
        return location_object

    @staticmethod
    def add_location(object: mediaupdate.mediaUpdateType, programUrl: str, avType = None):
        if not object.locations:
            object.locations = pyxb.BIND()

        location = MediaBackendUtil.create_location(programUrl, avType)
        object.locations.append(location)
        return location

    @staticmethod
    def member_of(object: mediaupdate.mediaUpdateType, group: str, position = 1):
        memberOf = mediaupdate.memberRefUpdateType(group)
        memberOf.highlighted = False
        memberOf.position = position
        object.memberOf.append(memberOf)

