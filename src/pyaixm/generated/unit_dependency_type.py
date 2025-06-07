from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_unit_dependency_type import CodeUnitDependencyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.unit_dependency_type_extension import (
    UnitDependencyTypeExtension,
)
from pyaixm.generated.unit_property_type import UnitPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitDependencyType(AbstractAixmobjectType):
    type_value: Optional[CodeUnitDependencyType] = field(
        default=None,
        metadata={
            "name": "type",
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
    the_unit: Optional[UnitPropertyType] = field(
        default=None,
        metadata={
            "name": "theUnit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[UnitDependencyTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
