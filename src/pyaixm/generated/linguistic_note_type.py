from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.linguistic_note_type_extension import (
    LinguisticNoteTypeExtension,
)
from pyaixm.generated.text_note_type import TextNoteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LinguisticNoteType(AbstractAixmobjectType):
    note: Optional[TextNoteType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[LinguisticNoteTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
