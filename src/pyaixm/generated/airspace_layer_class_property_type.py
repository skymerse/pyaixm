from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.airspace_layer_class import AirspaceLayerClass

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceLayerClassPropertyType(AbstractAixmpropertyType):
    airspace_layer_class: Optional[AirspaceLayerClass] = field(
        default=None,
        metadata={
            "name": "AirspaceLayerClass",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
