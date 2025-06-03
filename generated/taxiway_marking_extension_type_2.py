from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_cardinal_direction_type import CodeCardinalDirectionType
from generated.code_marking_status_type import CodeMarkingStatusType
from generated.code_taxiway_marking_type import CodeTaxiwayMarkingType
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class TaxiwayMarkingExtensionType2(AbstractExtensionType):
    class Meta:
        name = "TaxiwayMarkingExtensionType"

    type_value: Optional[CodeTaxiwayMarkingType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    status: Optional[CodeMarkingStatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
