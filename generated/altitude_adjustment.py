from dataclasses import dataclass

from generated.altitude_adjustment_type import AltitudeAdjustmentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltitudeAdjustment(AltitudeAdjustmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
