from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.aircraft_stand_property_type import AircraftStandPropertyType
from generated.apron_area_availability_property_type import (
    ApronAreaAvailabilityPropertyType,
)
from generated.apron_property_type import ApronPropertyType
from generated.deicing_area_time_slice_type_extension import (
    DeicingAreaTimeSliceTypeExtension,
)
from generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from generated.taxiway_property_type import TaxiwayPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaTimeSliceType(AbstractAixmtimeSliceType):
    associated_apron: Optional[ApronPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedApron",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    taxiway_location: Optional[TaxiwayPropertyType] = field(
        default=None,
        metadata={
            "name": "taxiwayLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    stand_location: Optional[AircraftStandPropertyType] = field(
        default=None,
        metadata={
            "name": "standLocation",
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
    extent: Optional[ElevatedSurfacePropertyType] = field(
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
    availability: Iterable[ApronAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[DeicingAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
