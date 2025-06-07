from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RouteSegmentExtensionType2(AbstractExtensionType):
    class Meta:
        name = "RouteSegmentExtensionType"

    state_territory: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "stateTerritory",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
