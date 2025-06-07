from dataclasses import dataclass

from pyaixm.generated.altimeter_source_type import AltimeterSourceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSource(AltimeterSourceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
