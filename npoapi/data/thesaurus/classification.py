from dataclasses import dataclass
from .classification_type import ClassificationType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Classification(ClassificationType):
    class Meta:
        name = "classification"
        namespace = "urn:vpro:gtaa:2017"
