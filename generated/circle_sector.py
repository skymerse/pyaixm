from dataclasses import dataclass

from generated.circle_sector_type import CircleSectorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CircleSector(CircleSectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
