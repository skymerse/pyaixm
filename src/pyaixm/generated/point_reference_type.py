from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.angle_use_property_type import AngleUsePropertyType
from generated.code_reference_role_type import CodeReferenceRoleType
from generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from generated.distance_indication_property_type import (
    DistanceIndicationPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.point_reference_type_extension import (
    PointReferenceTypeExtension,
)
from generated.surface_property_type_2 import SurfacePropertyType2
from generated.val_distance_signed_type import ValDistanceSignedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PointReferenceType(AbstractAixmobjectType):
    role: Optional[CodeReferenceRoleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    prior_fix_tolerance: Optional[ValDistanceSignedType] = field(
        default=None,
        metadata={
            "name": "priorFixTolerance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    post_fix_tolerance: Optional[ValDistanceSignedType] = field(
        default=None,
        metadata={
            "name": "postFixTolerance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    point: Optional[DesignatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    facility_angle: Iterable[AngleUsePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "facilityAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    facility_distance: Iterable[DistanceIndicationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "facilityDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    fix_tolerance_area: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "name": "fixToleranceArea",
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
    extension: Iterable[PointReferenceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
