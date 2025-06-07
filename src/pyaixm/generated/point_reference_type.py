from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.angle_use_property_type import AngleUsePropertyType
from pyaixm.generated.code_reference_role_type import CodeReferenceRoleType
from pyaixm.generated.designated_point_property_type import (
    DesignatedPointPropertyType,
)
from pyaixm.generated.distance_indication_property_type import (
    DistanceIndicationPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.point_reference_type_extension import (
    PointReferenceTypeExtension,
)
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2
from pyaixm.generated.val_distance_signed_type import ValDistanceSignedType

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
