from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.nitrogen import Nitrogen

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NitrogenPropertyType(AbstractAixmpropertyType):
    nitrogen: Optional[Nitrogen] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
