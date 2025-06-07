from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.manoeuvring_area_availability import (
    ManoeuvringAreaAvailability,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaAvailabilityPropertyType(AbstractAixmpropertyType):
    manoeuvring_area_availability: Optional[ManoeuvringAreaAvailability] = (
        field(
            default=None,
            metadata={
                "name": "ManoeuvringAreaAvailability",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
