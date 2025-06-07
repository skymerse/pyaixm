from dataclasses import dataclass

from generated.meteorology_type import MeteorologyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Meteorology(MeteorologyType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
