from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airspace_volume_dependency import (
    AirspaceVolumeDependency,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceVolumeDependencyPropertyType(AbstractAixmpropertyType):
    airspace_volume_dependency: Optional[AirspaceVolumeDependency] = field(
        default=None,
        metadata={
            "name": "AirspaceVolumeDependency",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
