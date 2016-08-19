#!/usr/bin/env python3
import unittest
import dateutil.parser

from npoapi import TranscodingUtil as TU


class Tests(unittest.TestCase):




    def test_parse_duration(self):
        exifinfo= {'Media Create Date': '0000:00:00 00:00:00', 'Op Color': '0 0 0',
                   'Track Modify Date': '0000:00:00 00:00:00', 'Selection Duration': '0 s', 'Image Height': '270',
                   'Track Layer': '0', 'Media Duration': '0:20:22', 'Handler Vendor ID': 'Apple',
                   'Audio Bits Per Sample': '16', 'Source Image Width': '480', 'Next Track ID': '3',
                   'Video Frame Rate': '25', 'Poster Time': '0 s',
                   'File Inode Change Date/Time': '2016:08:19 15:41:25+02:00', 'Media Time Scale': '44100',
                   'Selection Time': '0 s', 'ExifTool Version Number': '9.46',
                   'Track Create Date': '0000:00:00 00:00:00', 'Movie Header Version': '0', 'Handler Type': 'Metadata',
                   'Avg Bitrate': '537 kbps', 'Preferred Rate': '1', 'Source Image Height': '270',
                   'Graphics Mode': 'srcCopy', 'Major Brand': 'MP4  Base Media v1 [IS0 14496-12:2003]',
                   'Preview Duration': '0 s', 'Media Language Code': 'und',
                   'File Modification Date/Time': '2016:08:19 15:41:25+02:00', 'File Permissions': 'rw-rw-r--',
                   'Encoder': 'Lavf54.25.104', 'Media Header Version': '0', 'Time Scale': '1000',
                   'MIME Type': 'video/mp4', 'Track ID': '1', 'Directory': '/tmp', 'Audio Format': 'mp4a',
                   'Y Resolution': '72', 'Media Modify Date': '0000:00:00 00:00:00', 'Audio Sample Rate': '44100',
                   'Rotation': '0', 'Movie Data Offset': '48', 'Movie Data Size': '81967518',
                   'Handler Description': 'SoundHandler', 'Modify Date': '0000:00:00 00:00:00',
                   'File Name': 'cinema_cannes2007_051707.mp4', 'X Resolution': '72', 'Preferred Volume': '100.00%',
                   'Current Time': '0 s', 'Compressor ID': 'avc1', 'Matrix Structure': '1 0 0 0 1 0 0 0 1',
                   'Duration': '0:20:22', 'Track Header Version': '0', 'File Type': 'MP4',
                   'Create Date': '0000:00:00 00:00:00', 'Bit Depth': '24', 'Track Volume': '0.00%',
                   'Track Duration': '0:20:22', 'Minor Version': '0.2.0', 'Compatible Brands': 'isom, iso2, avc1, mp41',
                   'Audio Channels': '2', 'Balance': '0', 'Image Width': '480', 'Preview Time': '0 s',
                   'File Size': '79 MB', 'Image Size': '480x270', 'File Access Date/Time': '2016:08:19 15:35:33+02:00'}
        duration = TU.exiftool_duration(exifinfo)
        self.assertEquals(1222000, duration)

