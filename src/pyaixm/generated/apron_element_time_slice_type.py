from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_supplies_service_property_type import (
    AirportSuppliesServicePropertyType,
)
from pyaixm.generated.apron_area_availability_property_type import (
    ApronAreaAvailabilityPropertyType,
)
from pyaixm.generated.apron_element_time_slice_type_extension import (
    ApronElementTimeSliceTypeExtension,
)
from pyaixm.generated.apron_property_type import ApronPropertyType
from pyaixm.generated.code_apron_element_type import CodeApronElementType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronElementTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeApronElementType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    jetway_availability: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "jetwayAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    towing_availability: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "towingAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    docking_availability: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "dockingAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    ground_power_availability: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "groundPowerAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_apron: Optional[ApronPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedApron",
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
    supply_service: Iterable[AirportSuppliesServicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "supplyService",
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
    extension: Iterable[ApronElementTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
