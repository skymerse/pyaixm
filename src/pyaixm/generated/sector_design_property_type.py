from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.sector_design import SectorDesign

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SectorDesignPropertyType(AbstractAixmpropertyType):
    sector_design: Optional[SectorDesign] = field(
        default=None,
        metadata={
            "name": "SectorDesign",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
