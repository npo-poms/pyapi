from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "urn:vpro:api:constraint:page:2013"


@dataclass(slots=True)
class Not:
    class Meta:
        name = "not"

    choice: Optional[Union["And", "Or", "Not", str]] = field(
        default=None,
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
                    "name": "not",
                    "type": Type["Not"],
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
        },
    )


@dataclass(slots=True)
class Or:
    class Meta:
        name = "or"

    choice: List[Union["And", "Or", Not, str]] = field(
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
                    "name": "not",
                    "type": Not,
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
        },
    )


@dataclass(slots=True)
class And:
    class Meta:
        name = "and"

    choice: List[Union["And", Or, Not, str]] = field(
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
                    "name": "not",
                    "type": Not,
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
        },
    )


@dataclass(slots=True)
class Filter:
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:page:2013"

    choice: Optional[Union[And, Or, Not, str]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": And,
                },
                {
                    "name": "or",
                    "type": Or,
                },
                {
                    "name": "not",
                    "type": Not,
                },
                {
                    "name": "broadcaster",
                    "type": str,
                },
                {
                    "name": "type",
                    "type": str,
                },
                {
                    "name": "portal",
                    "type": str,
                },
                {
                    "name": "section",
                    "type": str,
                },
                {
                    "name": "genre",
                    "type": str,
                },
            ),
        },
    )
