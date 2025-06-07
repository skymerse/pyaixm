from dataclasses import dataclass

from pyaixm.generated.reflector_type import ReflectorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Reflector(ReflectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
