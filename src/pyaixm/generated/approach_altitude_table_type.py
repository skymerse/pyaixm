from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.approach_altitude_table_type_extension import (
    ApproachAltitudeTableTypeExtension,
)
from pyaixm.generated.code_procedure_distance_type import (
    CodeProcedureDistanceType,
)
from pyaixm.generated.code_vertical_reference_type import (
    CodeVerticalReferenceType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

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
