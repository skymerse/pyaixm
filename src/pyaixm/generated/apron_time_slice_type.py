from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.apron_area_availability_property_type import (
    ApronAreaAvailabilityPropertyType,
)
from pyaixm.generated.apron_contamination_property_type import (
    ApronContaminationPropertyType,
)
from pyaixm.generated.apron_time_slice_type_extension import (
    ApronTimeSliceTypeExtension,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
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
    contaminant: Iterable[ApronContaminationPropertyType] = field(
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
    extension: Iterable[ApronTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
