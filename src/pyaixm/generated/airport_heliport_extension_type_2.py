from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_extension_type import AbstractExtensionType
from generated.text_name_type import TextNameType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportHeliportExtensionType2(AbstractExtensionType):
    class Meta:
        name = "AirportHeliportExtensionType"

    state_territory: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "stateTerritory",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
