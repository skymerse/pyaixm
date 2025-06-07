from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportHeliportAvailabilityExtensionType(AbstractExtensionType):
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    warning_adjacent: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "warningAdjacent",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
