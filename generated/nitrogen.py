from dataclasses import dataclass

from generated.nitrogen_type import NitrogenType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Nitrogen(NitrogenType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
