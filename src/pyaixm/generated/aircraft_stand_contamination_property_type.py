from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.aircraft_stand_contamination import AircraftStandContamination

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandContaminationPropertyType(AbstractAixmpropertyType):
    aircraft_stand_contamination: Optional[AircraftStandContamination] = field(
        default=None,
        metadata={
            "name": "AircraftStandContamination",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
