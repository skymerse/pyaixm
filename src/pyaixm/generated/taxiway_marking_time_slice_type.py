from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_marking_condition_type import (
    CodeMarkingConditionType,
)
from pyaixm.generated.code_taxiway_section_type import CodeTaxiwaySectionType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.marking_element_property_type import (
    MarkingElementPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.taxiway_element_property_type import (
    TaxiwayElementPropertyType,
)
from pyaixm.generated.taxiway_marking_time_slice_type_extension import (
    TaxiwayMarkingTimeSliceTypeExtension,
)
from pyaixm.generated.taxiway_property_type import TaxiwayPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayMarkingTimeSliceType(AbstractAixmtimeSliceType):
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
    marking_location: Optional[CodeTaxiwaySectionType] = field(
        default=None,
        metadata={
            "name": "markingLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marked_taxiway: Optional[TaxiwayPropertyType] = field(
        default=None,
        metadata={
            "name": "markedTaxiway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marked_element: Optional[TaxiwayElementPropertyType] = field(
        default=None,
        metadata={
            "name": "markedElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TaxiwayMarkingTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
