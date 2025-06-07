from dataclasses import dataclass

from pyaixm.generated.aerial_refuelling_anchor_type import (
    AerialRefuellingAnchorType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingAnchor(AerialRefuellingAnchorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
