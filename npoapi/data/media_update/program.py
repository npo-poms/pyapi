from dataclasses import dataclass
from .program_update_type import ProgramUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Program(ProgramUpdateType):
    class Meta:
        name = "program"
        namespace = "urn:vpro:media:update:2009"
