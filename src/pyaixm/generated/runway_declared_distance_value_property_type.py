from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.runway_declared_distance_value import (
    RunwayDeclaredDistanceValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDeclaredDistanceValuePropertyType(AbstractAixmpropertyType):
    runway_declared_distance_value: Optional[RunwayDeclaredDistanceValue] = (
        field(
            default=None,
            metadata={
                "name": "RunwayDeclaredDistanceValue",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
