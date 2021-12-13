#!/usr/bin/env python3
import json
import os
import unittest

from ijson import items

from npoapi import Media
from npoapi import Subtitles

ENV = "acc"
MID = "WO_VPRO_783763"
CONFIG_DIR=os.path.dirname(os.path.dirname(__file__))
DEBUG=False


class MediaTests(unittest.TestCase):
    def test_get(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.get("AVRO_1656037"))
        self.assertEqual(result["mid"], "AVRO_1656037")

    def test_get_quote(self):
        client = self.get_client()
        result = client.get(" Avro_1260864")
        self.assertEqual(None, result)
        self.assertEqual(404, client.code)

    def test_get_space(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.get("BNN 240466"))
        self.assertEqual(result["mid"], "BNN 240466")

    def test_list(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.list())
        ""

    def test_search(self):
        client = self.get_client()
        result = json.JSONDecoder().decode(client.search("{}"))
        ""

    def test_stream(self):
        from datetime import datetime
        client = self.get_client()
        objects:items = client.changes()
        for o in objects:
            media = o["media"]
            if "sortDate" in media:
                sort_date = datetime.fromtimestamp(media["sortDate"] / 1e3)
                print(media["broadcasters"], sort_date)
            else:
                print(media["broadcasters"])

    def test(self):
        import datetime
        dates = [datetime.date(2016, 1, 31), datetime.date(2016, 1, 30), datetime.date(2016, 2, 1)]
        sorted(dates)
        print(dates)

    def get_client(self):
        print(os.path.dirname(__file__))
        return Media().configured_login(config_dir=CONFIG_DIR).env(ENV).debug(DEBUG)


class SubtitlesTest(unittest.TestCase):

    def test_get(self):
        client_sub = Subtitles(env='test').configured_login(create_config_file=True)
        client_sub.get(mid="POW_03689995", language='nl', subtitle_type='CAPTION')
        client_sub = Subtitles(env='test').configured_login(create_config_file=True)
        print(client_sub.get(mid="POW_03689995", language='nl', subtitle_type='CAPTION'))

