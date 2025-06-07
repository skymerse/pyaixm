from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_location_qualifier_type import (
    CodeLocationQualifierType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.flight_condition_circumstance_type_extension import (
    FlightConditionCircumstanceTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightConditionCircumstanceType(AbstractAixmobjectType):
    reference_location: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "referenceLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    relation_with_location: Optional[CodeLocationQualifierType] = field(
        default=None,
        metadata={
            "name": "relationWithLocation",
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
    extension: Iterable[FlightConditionCircumstanceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
