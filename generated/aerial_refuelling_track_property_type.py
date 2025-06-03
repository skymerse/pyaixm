from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.aerial_refuelling_track import AerialRefuellingTrack

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTrackPropertyType(AbstractAixmpropertyType):
    aerial_refuelling_track: Optional[AerialRefuellingTrack] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
