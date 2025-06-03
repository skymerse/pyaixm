from dataclasses import dataclass

from generated.angle_indication_type import AngleIndicationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleIndication(AngleIndicationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
