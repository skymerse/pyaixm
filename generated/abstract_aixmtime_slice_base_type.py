from dataclasses import dataclass, field
from typing import Any

from generated.abstract_time_slice_type import AbstractTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmtimeSliceBaseType(AbstractTimeSliceType):
    """Base type of AIXM Timeslices.

    Removes option attributes that are not used in AIXM.
    """

    class Meta:
        name = "AbstractAIXMTimeSliceBaseType"

    data_source: Any = field(
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
    opengis_net_gml_3_2_description: Any = field(
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
    identifier: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    opengis_net_gml_3_2_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
