from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.linguistic_note import LinguisticNote

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LinguisticNotePropertyType(AbstractAixmpropertyType):
    linguistic_note: Optional[LinguisticNote] = field(
        default=None,
        metadata={
            "name": "LinguisticNote",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
