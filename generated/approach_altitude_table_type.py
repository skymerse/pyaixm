from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.approach_altitude_table_type_extension import (
    ApproachAltitudeTableTypeExtension,
)
from generated.code_procedure_distance_type import CodeProcedureDistanceType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.note_property_type import NotePropertyType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachAltitudeTableType(AbstractAixmobjectType):
    measurement_point: Optional[CodeProcedureDistanceType] = field(
        default=None,
        metadata={
            "name": "measurementPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "altitudeReference",
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
    extension: Iterable[ApproachAltitudeTableTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
