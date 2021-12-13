from dataclasses import dataclass
from .media_form_type import MediaFormType

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:media:search:2012"
