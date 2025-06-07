from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.aerial_refuelling_anchor_type_extension import (
    AerialRefuellingAnchorTypeExtension,
)
from pyaixm.generated.aerial_refuelling_point_property_type import (
    AerialRefuellingPointPropertyType,
)
from pyaixm.generated.airspace_layer_property_type import (
    AirspaceLayerPropertyType,
)
from pyaixm.generated.code_course_type import CodeCourseType
from pyaixm.generated.code_direction_turn_type import CodeDirectionTurnType
from pyaixm.generated.code_vertical_reference_type import (
    CodeVerticalReferenceType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingAnchorType(AbstractAixmobjectType):
    outbound_course: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "outboundCourse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_course_type: Optional[CodeCourseType] = field(
        default=None,
        metadata={
            "name": "outboundCourseType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    inbound_course: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "inboundCourse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    turn_direction: Optional[CodeDirectionTurnType] = field(
        default=None,
        metadata={
            "name": "turnDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_limit: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "name": "speedLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_separation: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "legSeparation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "legLength",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    refuelling_base_level: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "refuellingBaseLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    refuelling_base_level_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "refuellingBaseLevelReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    extent: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_extent: Iterable[AirspaceLayerPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "verticalExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point: Iterable[AerialRefuellingPointPropertyType] = field(
        default_factory=list,
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
    extension: Iterable[AerialRefuellingAnchorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
