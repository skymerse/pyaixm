from dataclasses import dataclass

from pyaixm.generated.linguistic_note_type import LinguisticNoteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LinguisticNote(LinguisticNoteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
