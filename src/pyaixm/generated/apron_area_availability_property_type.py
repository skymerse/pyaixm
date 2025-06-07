from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.apron_area_availability import ApronAreaAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronAreaAvailabilityPropertyType(AbstractAixmpropertyType):
    apron_area_availability: Optional[ApronAreaAvailability] = field(
        default=None,
        metadata={
            "name": "ApronAreaAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
