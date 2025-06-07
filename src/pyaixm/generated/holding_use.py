from dataclasses import dataclass

from pyaixm.generated.holding_use_type import HoldingUseType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingUse(HoldingUseType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
