from dataclasses import dataclass

from generated.aerial_refuelling_track_type import AerialRefuellingTrackType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTrack(AerialRefuellingTrackType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
