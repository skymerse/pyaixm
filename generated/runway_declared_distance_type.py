from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_declared_distance_type import CodeDeclaredDistanceType
from generated.note_property_type import NotePropertyType
from generated.runway_declared_distance_type_extension import (
    RunwayDeclaredDistanceTypeExtension,
)
from generated.runway_declared_distance_value_property_type import (
    RunwayDeclaredDistanceValuePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDeclaredDistanceType(AbstractAixmobjectType):
    type_value: Optional[CodeDeclaredDistanceType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    declared_value: Iterable[RunwayDeclaredDistanceValuePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "declaredValue",
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
    extension: Iterable[RunwayDeclaredDistanceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
