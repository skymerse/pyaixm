from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.text_note_type import TextNoteType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwaySectionContaminationExtensionType(AbstractExtensionType):
    runway_condition_code: Optional[TextNoteType] = field(
        default=None,
        metadata={
            "name": "runwayConditionCode",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
