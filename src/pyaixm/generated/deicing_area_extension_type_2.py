from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class DeicingAreaExtensionType2(AbstractExtensionType):
    class Meta:
        name = "DeicingAreaExtensionType"

    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
