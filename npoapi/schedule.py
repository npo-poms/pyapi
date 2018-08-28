from npoapi.npoapi import NpoApi


class Schedule(NpoApi):
    def get(self, guideDay=None, channel=None):
        params = {
            'guideDay': guideDay
        }
        if channel:
            return self.request("/api/schedule/channel/" + channel, params=params)
        else:
            return self.request("/api/schedule", params=params)

    def search(self, form="{}", sort="asc", offset=0, limit=240, profile=None, properties=None, accept=None):
        return self.request("/api/schedule/", data=form, accept=accept, params={"profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties})
