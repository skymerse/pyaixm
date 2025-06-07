from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.approach_condition_property_type import (
    ApproachConditionPropertyType,
)
from pyaixm.generated.circling_area_time_slice_type_extension import (
    CirclingAreaTimeSliceTypeExtension,
)
from pyaixm.generated.instrument_approach_procedure_property_type import (
    InstrumentApproachProcedurePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingAreaTimeSliceType(AbstractAixmtimeSliceType):
    extent: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach: Optional[InstrumentApproachProcedurePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    condition: Iterable[ApproachConditionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft_category: Optional[AircraftCharacteristicPropertyType] = field(
        default=None,
        metadata={
            "name": "aircraftCategory",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    design_surface: Iterable[ObstacleAssessmentAreaPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "designSurface",
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
    extension: Iterable[CirclingAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
