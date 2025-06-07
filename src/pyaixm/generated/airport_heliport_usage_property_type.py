from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airport_heliport_usage import AirportHeliportUsage

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportUsagePropertyType(AbstractAixmpropertyType):
    airport_heliport_usage: Optional[AirportHeliportUsage] = field(
        default=None,
        metadata={
            "name": "AirportHeliportUsage",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
