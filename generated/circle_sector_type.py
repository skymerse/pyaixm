from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.circle_sector_type_extension import CircleSectorTypeExtension
from generated.code_arc_direction_type import CodeArcDirectionType
from generated.code_bearing_type import CodeBearingType
from generated.code_direction_reference_type import CodeDirectionReferenceType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.note_property_type import NotePropertyType
from generated.val_bearing_type import ValBearingType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CircleSectorType(AbstractAixmobjectType):
    arc_direction: Optional[CodeArcDirectionType] = field(
        default=None,
        metadata={
            "name": "arcDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    from_angle: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "fromAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    to_angle: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "toAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_type: Optional[CodeBearingType] = field(
        default=None,
        metadata={
            "name": "angleType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle_direction_reference: Optional[CodeDirectionReferenceType] = field(
        default=None,
        metadata={
            "name": "angleDirectionReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    inner_distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "innerDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outer_distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "outerDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "upperLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "lowerLimitReference",
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
    extension: Iterable[CircleSectorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
