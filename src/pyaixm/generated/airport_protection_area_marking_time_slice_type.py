from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.airport_heliport_protection_area_property_type import (
    AirportHeliportProtectionAreaPropertyType,
)
from pyaixm.generated.airport_protection_area_marking_time_slice_type_extension import (
    AirportProtectionAreaMarkingTimeSliceTypeExtension,
)
from pyaixm.generated.code_marking_condition_type import (
    CodeMarkingConditionType,
)
from pyaixm.generated.code_protect_area_section_type import (
    CodeProtectAreaSectionType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.marking_element_property_type import (
    MarkingElementPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportProtectionAreaMarkingTimeSliceType(AbstractAixmtimeSliceType):
    marking_icaostandard: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "markingICAOStandard",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    condition: Optional[CodeMarkingConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element: Iterable[MarkingElementPropertyType] = field(
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
    marking_location: Optional[CodeProtectAreaSectionType] = field(
        default=None,
        metadata={
            "name": "markingLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marked_protection_area: Optional[
        AirportHeliportProtectionAreaPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "markedProtectionArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[AirportProtectionAreaMarkingTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
