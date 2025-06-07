from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_stand_contamination_property_type import (
    AircraftStandContaminationPropertyType,
)
from pyaixm.generated.aircraft_stand_time_slice_type_extension import (
    AircraftStandTimeSliceTypeExtension,
)
from pyaixm.generated.apron_area_availability_property_type import (
    ApronAreaAvailabilityPropertyType,
)
from pyaixm.generated.apron_element_property_type import (
    ApronElementPropertyType,
)
from pyaixm.generated.code_aircraft_stand_type import CodeAircraftStandType
from pyaixm.generated.code_visual_docking_guidance_type import (
    CodeVisualDockingGuidanceType,
)
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.text_designator_type import TextDesignatorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeAircraftStandType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    visual_docking_system: Optional[CodeVisualDockingGuidanceType] = field(
        default=None,
        metadata={
            "name": "visualDockingSystem",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_properties: Optional[SurfaceCharacteristicsPropertyType] = field(
        default=None,
        metadata={
            "name": "surfaceProperties",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    apron_location: Optional[ApronElementPropertyType] = field(
        default=None,
        metadata={
            "name": "apronLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contaminant: Iterable[AircraftStandContaminationPropertyType] = field(
        default_factory=list,
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
    availability: Iterable[ApronAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AircraftStandTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
