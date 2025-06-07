from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.airspace_geometry_component_type_extension import (
    AirspaceGeometryComponentTypeExtension,
)
from generated.airspace_volume_property_type import AirspaceVolumePropertyType
from generated.code_airspace_aggregation_type import (
    CodeAirspaceAggregationType,
)
from generated.no_sequence_type import NoSequenceType
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceGeometryComponentType(AbstractAixmobjectType):
    operation: Optional[CodeAirspaceAggregationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    operation_sequence: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "operationSequence",
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
    the_airspace_volume: Optional[AirspaceVolumePropertyType] = field(
        default=None,
        metadata={
            "name": "theAirspaceVolume",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[AirspaceGeometryComponentTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
