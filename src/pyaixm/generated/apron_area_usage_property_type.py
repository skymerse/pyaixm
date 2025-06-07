from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.apron_area_usage import ApronAreaUsage

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronAreaUsagePropertyType(AbstractAixmpropertyType):
    apron_area_usage: Optional[ApronAreaUsage] = field(
        default=None,
        metadata={
            "name": "ApronAreaUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
