from dataclasses import dataclass

from pyaixm.generated.dmetype import Dmetype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Dme(Dmetype):
    class Meta:
        name = "DME"
        namespace = "http://www.aixm.aero/schema/5.1"
