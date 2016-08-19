
import re
import logging
import subprocess
import urllib
import os
from fractions import Fraction


class TranscodingUtil(object):
    """A common use case for using the NPO backend api is trancoding 'locations'. This provides some utilities for doing that."""



    FFMEG = "ffmpeg"
    EXIFTOOL = "exiftool"

    logger = logging.getLogger("TranscodingUtil")

    @staticmethod
    def exiftool(file):
        command = [TranscodingUtil.EXIFTOOL, file]
        TranscodingUtil.logger.info("Calling %s", command)

        p = subprocess.Popen(command, stdin=None, stdout=subprocess.PIPE)

        result = {}
        while True:
            line = p.stdout.readline()
            if not line:
                break

            array = line.decode().strip().split(":", 1)
            result[array[0].strip()] = array[1].strip()
        return result

    @staticmethod
    def exiftool_aspectratio(info: dict):
        string = info.get('Image Size', None)
        if not string:
            return None
        else:
            a = string.split("x", 2)
            logging.info(str(a))
            f = Fraction(int(a[0]), int(a[1]))
            return str(f.numerator) + ":" + str(f.denominator)

    @staticmethod
    def exiftool_duration(info: dict):
        string = info.get('Media Duration', None)
        if not string:
            return None
        else:
            m = re.match("(.*) s", string)
            if m:
                return "P0DT" + m.group(1) + "S"
            a = string.split(":")
            return "P0DT" + a[0] + "H" + a[1] + "M" + a[2] + ".000S"

    @staticmethod
    def exiftool_parsebitrate(string: str):
        if not string:
            return None
        else:
            a = string.split(" ", 2)
            if len(a) == 1:
                return int(a[0].strip())
            else:
                if a[1].strip() == "Mbps":
                    return int(float(a[0].strip()) * 1000 * 1000)
                elif a[1].strip() == "kbps":
                    return int(float(a[0].strip()) * 1000)
                else:
                    TranscodingUtil.logger.warn("Unrecognized bitrate " + string)
                    return None


    @staticmethod
    def exiftool_bitrate(info: dict):
        avgbitrate = info.get("Avg Bitrate", None)
        audiobitrate = info.get("Audio Bitrate", None)
        result = None
        if avgbitrate:
            result = TranscodingUtil.exiftool_parsebitrate(avgbitrate)
        if not result:
            result = TranscodingUtil.exiftool_parsebitrate(audiobitrate)
        return result



    @staticmethod
    def system_call(command):
        TranscodingUtil.logger.info("Calling %s", command)
        exitcode = subprocess.call(command, shell=False, stderr=subprocess.STDOUT)
        TranscodingUtil.logger.info("Ready. Exitcode %s", str(exitcode))
        return exitcode

    @staticmethod
    def transcode(programUrl, tempFile):
        command = [TranscodingUtil.FFMEG,
                   "-y", "-loglevel", "warning",
                   "-i", programUrl,
                   "-profile:v", "main",
                   tempFile]
        TranscodingUtil.system_call(command)

    @staticmethod
    def ffmpeg_images(sourcefile, dest_dir, offsets=['00:01:00.000', '00:02:00.000', '00:03:00.000']):
        seq = 1
        result = []
        for offset in offsets:
            logging.info("offset " + offset)
            command = [TranscodingUtil.FFMEG, "-loglevel" "warning", "-i", sourcefile]
            image_file_name = os.path.join(dest_dir, "still." + str(seq) + ".jpg")
            command.extend(["-ss", offset,  "-vframes",  1,  image_file_name])
            TranscodingUtil.system_call(command)
            result.append([offset, image_file_name])
            seq += 1
        return result

    @staticmethod
    def check_exists(programUrl):
        request = urllib.request.Request(programUrl, method="HEAD")
        try:
            response = urllib.request.urlopen(request)
            if response.code == 200:
                return True
        except urllib.error.HTTPError as ue:
            if ue.code == 404:
                return False
            else:
                raise


