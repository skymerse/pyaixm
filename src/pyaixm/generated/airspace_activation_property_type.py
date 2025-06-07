from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.airspace_activation import AirspaceActivation

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceActivationPropertyType(AbstractAixmpropertyType):
    airspace_activation: Optional[AirspaceActivation] = field(
        default=None,
        metadata={
            "name": "AirspaceActivation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
