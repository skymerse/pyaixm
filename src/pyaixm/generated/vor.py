from dataclasses import dataclass

from pyaixm.generated.vortype import Vortype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Vor(Vortype):
    class Meta:
        name = "VOR"
        namespace = "http://www.aixm.aero/schema/5.1"
