from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class SurfaceContaminationLayerExtensionType(AbstractExtensionType):
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    contaminant_length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "contaminantLength",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
