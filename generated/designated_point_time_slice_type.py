from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_designated_point_designator_type import (
    CodeDesignatedPointDesignatorType,
)
from generated.code_designated_point_type import CodeDesignatedPointType
from generated.designated_point_time_slice_type_extension import (
    DesignatedPointTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.point_property_type_2 import PointPropertyType2
from generated.runway_centreline_point_property_type import (
    RunwayCentrelinePointPropertyType,
)
from generated.text_name_type import TextNameType
from generated.touch_down_lift_off_property_type import (
    TouchDownLiftOffPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DesignatedPointTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[CodeDesignatedPointDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeDesignatedPointType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[PointPropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aiming_point: Optional[TouchDownLiftOffPropertyType] = field(
        default=None,
        metadata={
            "name": "aimingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    airport_heliport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "airportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    runway_point: Optional[RunwayCentrelinePointPropertyType] = field(
        default=None,
        metadata={
            "name": "runwayPoint",
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
    extension: Iterable[DesignatedPointTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
