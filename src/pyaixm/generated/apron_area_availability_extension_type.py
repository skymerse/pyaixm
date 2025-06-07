from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_apron_section_type import CodeApronSectionType
from pyaixm.generated.code_barrier_type import CodeBarrierType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ApronAreaAvailabilityExtensionType(AbstractExtensionType):
    warning_adjacent: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "warningAdjacent",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "warningDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_section: Optional[CodeApronSectionType] = field(
        default=None,
        metadata={
            "name": "warningSection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_barrier: Optional[CodeBarrierType] = field(
        default=None,
        metadata={
            "name": "warningBarrier",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "warningLength",
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
