from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.service_usage_property_type import (
    ServiceUsagePropertyType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ServiceExtensionType2(AbstractExtensionType):
    class Meta:
        name = "ServiceExtensionType"

    limit: Optional[ServiceUsagePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
