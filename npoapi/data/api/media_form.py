from dataclasses import dataclass
from .media_form_type import MediaFormType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:api:2013"
