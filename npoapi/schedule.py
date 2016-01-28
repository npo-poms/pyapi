from npoapi.npoapi import NpoApi

#import urllib.request

class Schedule(NpoApi):
    def get(self, guideDay=None, channel=None):
        params = {
            'guideDay': guideDay
        }
        if channel:
            return self.request("/api/schedule/" + channel, params=params)
        else:
            return self.request("/api/schedule", params=params)

