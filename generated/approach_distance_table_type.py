from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.approach_distance_table_type_extension import (
    ApproachDistanceTableTypeExtension,
)
from generated.code_procedure_distance_type import CodeProcedureDistanceType
from generated.note_property_type import NotePropertyType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachDistanceTableType(AbstractAixmobjectType):
    starting_measurement_point: Optional[CodeProcedureDistanceType] = field(
        default=None,
        metadata={
            "name": "startingMeasurementPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    value_hat: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "valueHAT",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    ending_measurement_point: Optional[CodeProcedureDistanceType] = field(
        default=None,
        metadata={
            "name": "endingMeasurementPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    distance: Optional[ValDistanceType] = field(
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
    extension: Iterable[ApproachDistanceTableTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
