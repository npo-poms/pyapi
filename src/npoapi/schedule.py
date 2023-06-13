from typing import Optional

from npoapi.npoapi import NpoApi


class Schedule(NpoApi):
    def get_schedule_response(self, guideDay=None, channel=None,  sort="asc", offset=0, limit=240, properties=None, accept=None) -> Optional[str]:
        params = {
            'guideDay': guideDay,
            "sort": sort,
            "max": limit,
            "offset": offset,
            "properties": properties
        }
        if channel:
            return self.stream("/api/schedule/channel/" + channel, params=params, accept=accept)
        else:
            return self.stream("/api/schedule", params=params)
        
        
    def get_object(self, guideDay=None, channel=None,  sort="asc", offset=0, limit=240, properties=None):
        response = self.get_schedule_response(guideDay, channel, sort, offset, limit, properties, accept="application/xml")
        
       

    def get(self,  guideDay=None, channel=None,  sort="asc", offset=0, limit=240, properties=None, accept=None):
        response = self.get_schedule_response(guideDay, channel, sort, offset, limit, properties, accept)
        if response:
            return response.read().decode('utf-8')
        return None

    def search(self, form="{}", sort="asc", offset=0, limit=240, profile=None, properties=None, accept=None):
        return self.request("/api/schedule/", data=form, accept=accept, params={
        "profile": profile, "sort": sort, "offset": offset, "max": limit, "properties": properties}
                            )
