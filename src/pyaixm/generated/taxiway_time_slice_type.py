from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_taxiway_type import CodeTaxiwayType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.manoeuvring_area_availability_property_type import (
    ManoeuvringAreaAvailabilityPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.taxiway_contamination_property_type import (
    TaxiwayContaminationPropertyType,
)
from pyaixm.generated.taxiway_time_slice_type_extension import (
    TaxiwayTimeSliceTypeExtension,
)
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeTaxiwayType] = field(
        default=None,
        metadata={
            "name": "type",
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
    width_shoulder: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "widthShoulder",
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
    abandoned: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
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
    associated_airport_heliport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "associatedAirportHeliport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    contaminant: Iterable[TaxiwayContaminationPropertyType] = field(
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
    availability: Iterable[ManoeuvringAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TaxiwayTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
