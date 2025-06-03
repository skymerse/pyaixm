from dataclasses import dataclass, field
from typing import Any

from generated.dynamic_feature_type import DynamicFeatureType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmfeatureBaseType(DynamicFeatureType):
    """This derives from gml:DynamicFeatureType, as all AIXM features are expected
    to have temporal properties modeled using the Timeslice model.

    While the GML specification does not mandate that dynamic features
    derive from gml:DynamicFeatureType, many GML-aware applications may
    only detect a dynamic feature by this type hierarchy. Note that all
    temporal properties of gml:DynamicFeatureType are removed during
    this restriction, because they will be added for each AIXM feature
    specifically, based on the TimeSlice model
    """

    class Meta:
        name = "AbstractAIXMFeatureBaseType"

    valid_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    track: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    history: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    data_source: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    data_source_reference: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    meta_data_property: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description_reference: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
