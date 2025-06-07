from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.route_portion import RoutePortion

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RoutePortionPropertyType(AbstractAixmpropertyType):
    route_portion: Optional[RoutePortion] = field(
        default=None,
        metadata={
            "name": "RoutePortion",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
