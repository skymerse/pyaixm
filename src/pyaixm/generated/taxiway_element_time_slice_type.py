from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_grade_separation_type import CodeGradeSeparationType
from pyaixm.generated.code_taxiway_element_type import CodeTaxiwayElementType
from pyaixm.generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from pyaixm.generated.manoeuvring_area_availability_property_type import (
    ManoeuvringAreaAvailabilityPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.taxiway_element_time_slice_type_extension import (
    TaxiwayElementTimeSliceTypeExtension,
)
from pyaixm.generated.taxiway_property_type import TaxiwayPropertyType
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayElementTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeTaxiwayElementType] = field(
        default=None,
        metadata={
            "name": "type",
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
    grade_separation: Optional[CodeGradeSeparationType] = field(
        default=None,
        metadata={
            "name": "gradeSeparation",
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
    associated_taxiway: Optional[TaxiwayPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedTaxiway",
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
    availability: Iterable[ManoeuvringAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TaxiwayElementTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
