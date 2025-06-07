from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.light_activation import LightActivation

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightActivationPropertyType(AbstractAixmpropertyType):
    light_activation: Optional[LightActivation] = field(
        default=None,
        metadata={
            "name": "LightActivation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
