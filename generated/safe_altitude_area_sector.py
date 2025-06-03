from dataclasses import dataclass

from generated.safe_altitude_area_sector_type import SafeAltitudeAreaSectorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaSector(SafeAltitudeAreaSectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
