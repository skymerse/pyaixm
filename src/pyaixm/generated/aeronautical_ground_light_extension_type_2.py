from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_status_operations_type import CodeStatusOperationsType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AeronauticalGroundLightExtensionType2(AbstractExtensionType):
    class Meta:
        name = "AeronauticalGroundLightExtensionType"

    operational_status: Optional[CodeStatusOperationsType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
