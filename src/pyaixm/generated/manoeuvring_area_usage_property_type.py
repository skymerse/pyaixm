from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.manoeuvring_area_usage import ManoeuvringAreaUsage

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaUsagePropertyType(AbstractAixmpropertyType):
    manoeuvring_area_usage: Optional[ManoeuvringAreaUsage] = field(
        default=None,
        metadata={
            "name": "ManoeuvringAreaUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
