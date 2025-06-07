from dataclasses import dataclass

from pyaixm.generated.obstruction_type import ObstructionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Obstruction(ObstructionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
