from dataclasses import dataclass, field
from typing import List, Type

__NAMESPACE__ = "urn:vpro:api:constraint:page:2013"


@dataclass
class Or:
    class Meta:
        name = "or"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": Type["And"],
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "or",
                    "type": Type["Or"],
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "broadcaster",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "type",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "portal",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "section",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "genre",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
            ),
        }
    )


@dataclass
class And:
    class Meta:
        name = "and"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": Type["And"],
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "or",
                    "type": Or,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "broadcaster",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "type",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "portal",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "section",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
                {
                    "name": "genre",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:page:2013",
                },
            ),
        }
    )
