from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_runway_type import CodeRunwayType
from generated.code_yes_no_type import CodeYesNoType
from generated.note_property_type import NotePropertyType
from generated.runway_contamination_property_type import (
    RunwayContaminationPropertyType,
)
from generated.runway_section_contamination_property_type import (
    RunwaySectionContaminationPropertyType,
)
from generated.runway_time_slice_type_extension import (
    RunwayTimeSliceTypeExtension,
)
from generated.surface_characteristics_property_type import (
    SurfaceCharacteristicsPropertyType,
)
from generated.text_designator_type import TextDesignatorType
from generated.val_distance_signed_type import ValDistanceSignedType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeRunwayType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    nominal_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "nominalLength",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "lengthAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    nominal_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "nominalWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "widthAccuracy",
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
    length_strip: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "lengthStrip",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width_strip: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "widthStrip",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length_offset: Optional[ValDistanceSignedType] = field(
        default=None,
        metadata={
            "name": "lengthOffset",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width_offset: Optional[ValDistanceSignedType] = field(
        default=None,
        metadata={
            "name": "widthOffset",
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
    overall_contaminant: Iterable[RunwayContaminationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "overallContaminant",
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
    area_contaminant: Iterable[RunwaySectionContaminationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "areaContaminant",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[RunwayTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
