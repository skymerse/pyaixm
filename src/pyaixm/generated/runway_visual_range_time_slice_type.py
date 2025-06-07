from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_rvrreading_type import CodeRvrreadingType
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from pyaixm.generated.runway_visual_range_time_slice_type_extension import (
    RunwayVisualRangeTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayVisualRangeTimeSliceType(AbstractAixmtimeSliceType):
    reading_position: Optional[CodeRvrreadingType] = field(
        default=None,
        metadata={
            "name": "readingPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_runway_direction: Iterable[RunwayDirectionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "associatedRunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[RunwayVisualRangeTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
