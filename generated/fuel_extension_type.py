from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_delivery_method_type import CodeDeliveryMethodType
from generated.code_status_service_type import CodeStatusServiceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FuelExtensionType(AbstractExtensionType):
    delivery_method: Optional[CodeDeliveryMethodType] = field(
        default=None,
        metadata={
            "name": "deliveryMethod",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    operational_status: Optional[CodeStatusServiceType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
