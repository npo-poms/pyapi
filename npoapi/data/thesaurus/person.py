from dataclasses import dataclass
from .person_type import PersonType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Person(PersonType):
    class Meta:
        name = "person"
        namespace = "urn:vpro:gtaa:2017"
