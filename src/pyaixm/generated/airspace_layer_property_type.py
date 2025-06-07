from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.airspace_layer import AirspaceLayer

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceLayerPropertyType(AbstractAixmpropertyType):
    airspace_layer: Optional[AirspaceLayer] = field(
        default=None,
        metadata={
            "name": "AirspaceLayer",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
