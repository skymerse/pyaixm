from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airspace_volume import AirspaceVolume

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceVolumePropertyType(AbstractAixmpropertyType):
    airspace_volume: Optional[AirspaceVolume] = field(
        default=None,
        metadata={
            "name": "AirspaceVolume",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
