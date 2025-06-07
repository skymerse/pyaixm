from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airspace_geometry_component import (
    AirspaceGeometryComponent,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceGeometryComponentPropertyType(AbstractAixmpropertyType):
    airspace_geometry_component: Optional[AirspaceGeometryComponent] = field(
        default=None,
        metadata={
            "name": "AirspaceGeometryComponent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
