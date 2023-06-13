#!/usr/bin/env python3
import json
import os
import unittest

from npoapi import Pages
from npoapi.data.api import PagesForm, PagesSearchType, TextMatcherListType, TextMatcherType

ENV = "acc"
CONFIG_DIR=os.path.dirname(os.path.dirname(__file__))
DEBUG=False


class PagesTest(unittest.TestCase):
    def test_search(self):
        client = self.get_client()
        form = PagesForm()
        form.searches = PagesSearchType()
        form.searches.types = TextMatcherListType()
        matcher = TextMatcherType()
        matcher.value = "HOME"
        form.searches.types.matcher = [matcher]
        result = client.search(form = form, profile = "vpro")
        result = json.JSONDecoder().decode(result)
        print(result)


    @staticmethod
    def get_client():
        print(os.path.dirname(__file__))
        return Pages().configured_login(config_dir=CONFIG_DIR).env(ENV).debug(DEBUG)

