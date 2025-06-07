from dataclasses import dataclass

from pyaixm.generated.unplanned_holding_type import UnplannedHoldingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnplannedHolding(UnplannedHoldingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
