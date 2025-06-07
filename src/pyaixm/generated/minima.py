from dataclasses import dataclass

from pyaixm.generated.minima_type import MinimaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Minima(MinimaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
