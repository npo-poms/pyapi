#!/usr/bin/env python3
import json
import unittest

from npoapi import Media
from npoapi import Screens
from npoapi.npoapi import NpoApi

ENV = "dev"


class Tests(unittest.TestCase):
    def test_authentication(self):
        client = NpoApi(origin="http://www.vpro.nl") \
            .login(key="a", secret="b")
        self.assertEqual("NPO a:CtHYR9a+nr17OIn5rYml6a+A9ujqe0IywWqr93/DAOk=",
                         client.authenticate(uri="/media", now="Fri, 30 Oct 2015 08:43:31 -0000")[0])


class MediaTests(unittest.TestCase):
    def test_get(self):
        client = Media().configured_login().env(ENV).debug()
        result = json.JSONDecoder().decode(client.get("AVRO_1656037"))
        self.assertEqual(result["mid"], "AVRO_1656037")

    def test_get_quote(self):
        client = Media().configured_login().env(ENV).debug()
        result = json.JSONDecoder().decode(client.get(" Avro_1260864"))
        self.assertEqual(result["mid"], " Avro_1260864")        

    def test_get_space(self):
        client = Media().configured_login().env(ENV).debug()
        result = json.JSONDecoder().decode(client.get("BNN 240466"))
        self.assertEqual(result["mid"], "BNN 240466")

    def test_list(self):
        client = Media().configured_login().env(ENV)
        result = json.JSONDecoder().decode(client.list())
        ""

    def test_search(self):
        client = Media().configured_login().env(ENV)
        result = json.JSONDecoder().decode(client.search("{}"))
        ""

    def test_stream(self):
        import ijson
        from datetime import datetime
        client = Media(env="test").configured_login(create_config_file=True)
        objects = ijson.items(client.changes(stream=True), 'changes.item')
        for o in objects:
            media = o["media"]
            sortDate = datetime.fromtimestamp(media["sortDate"] / 1e3)
            print(media["broadcasters"], sortDate)


    def test(self):
        import datetime
        dates = [datetime.date(2016, 1, 31), datetime.date(2016, 1, 30), datetime.date(2016, 2, 1)]
        sorted(dates)
        print(dates)


class ScreenTests(unittest.TestCase):
    def test_screens(self):
        client = Screens().configured_login().env(ENV)
        result = json.JSONDecoder().decode(client.list(offset=3))
        self.assertEqual(result["offset"], 3)
