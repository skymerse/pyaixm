from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.altitude_adjustment import AltitudeAdjustment

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltitudeAdjustmentPropertyType(AbstractAixmpropertyType):
    altitude_adjustment: Optional[AltitudeAdjustment] = field(
        default=None,
        metadata={
            "name": "AltitudeAdjustment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
