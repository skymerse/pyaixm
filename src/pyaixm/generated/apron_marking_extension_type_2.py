from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_apron_marking_type import CodeApronMarkingType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_landing_marking_type import CodeLandingMarkingType
from pyaixm.generated.code_marking_status_type import CodeMarkingStatusType
from pyaixm.generated.note_property_type import NotePropertyType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ApronMarkingExtensionType2(AbstractExtensionType):
    class Meta:
        name = "ApronMarkingExtensionType"

    marking_type: Optional[CodeApronMarkingType] = field(
        default=None,
        metadata={
            "name": "markingType",
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
    apron_marking_type: Optional[CodeLandingMarkingType] = field(
        default=None,
        metadata={
            "name": "apronMarkingType",
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
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
