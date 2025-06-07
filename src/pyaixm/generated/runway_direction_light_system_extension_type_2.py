from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_lighting_type import CodeLightingType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayDirectionLightSystemExtensionType2(AbstractExtensionType):
    class Meta:
        name = "RunwayDirectionLightSystemExtensionType"

    light_type: Optional[CodeLightingType] = field(
        default=None,
        metadata={
            "name": "lightType",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
