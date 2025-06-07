from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_note_purpose_type import CodeNotePurposeType
from pyaixm.generated.linguistic_note_property_type import (
    LinguisticNotePropertyType,
)
from pyaixm.generated.note_type_extension import NoteTypeExtension
from pyaixm.generated.text_property_name_type import TextPropertyNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NoteType(AbstractAixmobjectType):
    property_name: Optional[TextPropertyNameType] = field(
        default=None,
        metadata={
            "name": "propertyName",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    purpose: Optional[CodeNotePurposeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    translated_note: Iterable[LinguisticNotePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "translatedNote",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[NoteTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
