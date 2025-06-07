from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.code_navaid_designator_type import (
    CodeNavaidDesignatorType,
)
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class NavaidExtensionType2(AbstractExtensionType):
    class Meta:
        name = "NavaidExtensionType"

    broadcast_identifier: Optional[CodeNavaidDesignatorType] = field(
        default=None,
        metadata={
            "name": "broadcastIdentifier",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    state_territory: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "stateTerritory",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
