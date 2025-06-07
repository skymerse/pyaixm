from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_time_primitive_type import (
    TimeInstantPropertyType,
)
from pyaixm.generated.time_interval_length_type import TimeIntervalLengthType
from pyaixm.generated.time_position_type import TimePositionType
from pyaixm.generated.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCoordinateSystemType(TimeReferenceSystemType):
    origin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    origin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
