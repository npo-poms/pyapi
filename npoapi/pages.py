from npoapi.npoapi import NpoApi
import urllib.request

class Pages(NpoApi):
    def get(self, url):
        return self.request("/api/page/" + urllib.request.quote(url))
