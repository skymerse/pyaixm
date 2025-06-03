from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.fuel import Fuel

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FuelPropertyType(AbstractAixmpropertyType):
    fuel: Optional[Fuel] = field(
        default=None,
        metadata={
            "name": "Fuel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
