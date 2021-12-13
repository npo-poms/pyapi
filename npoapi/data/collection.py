from dataclasses import dataclass
from .collection_type import CollectionType


@dataclass
class Collection(CollectionType):
    class Meta:
        name = "collection"
