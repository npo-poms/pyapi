from dataclasses import dataclass
from .move_action_type import MoveActionType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Move(MoveActionType):
    class Meta:
        name = "move"
        namespace = "urn:vpro:media:update:2009"
