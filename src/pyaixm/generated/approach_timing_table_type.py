from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.approach_timing_table_type_extension import (
    ApproachTimingTableTypeExtension,
)
from pyaixm.generated.code_procedure_distance_type import (
    CodeProcedureDistanceType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_duration_type import ValDurationType
from pyaixm.generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachTimingTableType(AbstractAixmobjectType):
    starting_measurement_point: Optional[CodeProcedureDistanceType] = field(
        default=None,
        metadata={
            "name": "startingMeasurementPoint",
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
    time: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed: Optional[ValSpeedType] = field(
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
    extension: Iterable[ApproachTimingTableTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
