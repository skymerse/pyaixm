from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.airport_heliport_contamination import (
    AirportHeliportContamination,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportContaminationPropertyType(AbstractAixmpropertyType):
    airport_heliport_contamination: Optional[AirportHeliportContamination] = (
        field(
            default=None,
            metadata={
                "name": "AirportHeliportContamination",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
