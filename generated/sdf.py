from dataclasses import dataclass

from generated.sdftype import Sdftype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Sdf(Sdftype):
    class Meta:
        name = "SDF"
        namespace = "http://www.aixm.aero/schema/5.1"
