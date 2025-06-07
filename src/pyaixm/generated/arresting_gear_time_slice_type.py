from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.arresting_gear_time_slice_type_extension import (
    ArrestingGearTimeSliceTypeExtension,
)
from pyaixm.generated.code_arresting_gear_energy_absorb_type import (
    CodeArrestingGearEnergyAbsorbType,
)
from pyaixm.generated.code_arresting_gear_engage_device_type import (
    CodeArrestingGearEngageDeviceType,
)
from pyaixm.generated.code_status_operations_type import (
    CodeStatusOperationsType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.elevated_curve_property_type import (
    ElevatedCurvePropertyType,
)
from pyaixm.generated.elevated_point_property_type import (
    ElevatedPointPropertyType,
)
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrestingGearTimeSliceType(AbstractAixmtimeSliceType):
    status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
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
    engage_device: Optional[CodeArrestingGearEngageDeviceType] = field(
        default=None,
        metadata={
            "name": "engageDevice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    absorb_type: Optional[CodeArrestingGearEnergyAbsorbType] = field(
        default=None,
        metadata={
            "name": "absorbType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    bidirectional: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    runway_direction: Iterable[RunwayDirectionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "runwayDirection",
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
    extent_curve_extent: Optional[ElevatedCurvePropertyType] = field(
        default=None,
        metadata={
            "name": "extent_curveExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent_surface_extent: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "name": "extent_surfaceExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent_point_extent: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "name": "extent_pointExtent",
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
    extension: Iterable[ArrestingGearTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
