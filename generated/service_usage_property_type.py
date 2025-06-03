from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.service_usage import ServiceUsage

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ServiceUsagePropertyType(AbstractAixmpropertyType):
    service_usage: Optional[ServiceUsage] = field(
        default=None,
        metadata={
            "name": "ServiceUsage",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
