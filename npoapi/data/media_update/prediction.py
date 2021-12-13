from dataclasses import dataclass
from .prediction_update_type import PredictionUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Prediction(PredictionUpdateType):
    class Meta:
        name = "prediction"
        namespace = "urn:vpro:media:update:2009"
