from dataclasses import dataclass
from .boolean_predicate_test_result import BooleanPredicateTestResult

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


@dataclass
class OrPredicateTestResult(BooleanPredicateTestResult):
    class Meta:
        name = "orPredicateTestResult"
