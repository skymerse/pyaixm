from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.note import Note

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NotePropertyType(AbstractAixmpropertyType):
    note: Optional[Note] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
