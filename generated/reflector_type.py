from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_reflector_type import CodeReflectorType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.note_property_type import NotePropertyType
from generated.reflector_type_extension import ReflectorTypeExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ReflectorType(AbstractAixmobjectType):
    type_value: Optional[CodeReflectorType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    touchdown_reflector: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "touchdownReflector",
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
    extension: Iterable[ReflectorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
