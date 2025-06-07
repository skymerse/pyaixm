from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.unit_availability import UnitAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitAvailabilityPropertyType(AbstractAixmpropertyType):
    unit_availability: Optional[UnitAvailability] = field(
        default=None,
        metadata={
            "name": "UnitAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
