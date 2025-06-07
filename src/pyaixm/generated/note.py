from dataclasses import dataclass

from pyaixm.generated.note_type import NoteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Note(NoteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
