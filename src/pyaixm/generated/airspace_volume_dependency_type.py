from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.airspace_property_type import AirspacePropertyType
from generated.airspace_volume_dependency_type_extension import (
    AirspaceVolumeDependencyTypeExtension,
)
from generated.code_airspace_dependency_type import CodeAirspaceDependencyType
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceVolumeDependencyType(AbstractAixmobjectType):
    dependency: Optional[CodeAirspaceDependencyType] = field(
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
    the_airspace: Optional[AirspacePropertyType] = field(
        default=None,
        metadata={
            "name": "theAirspace",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[AirspaceVolumeDependencyTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
