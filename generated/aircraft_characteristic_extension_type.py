from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_value_interpretation_type import (
    CodeValueInterpretationType,
)
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AircraftCharacteristicExtensionType(AbstractExtensionType):
    tailheight_interpretation: Optional[CodeValueInterpretationType] = field(
        default=None,
        metadata={
            "name": "tailheightInterpretation",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    tailheight: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
