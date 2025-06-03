from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.meteorology import Meteorology

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MeteorologyPropertyType(AbstractAixmpropertyType):
    meteorology: Optional[Meteorology] = field(
        default=None,
        metadata={
            "name": "Meteorology",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
