from dataclasses import dataclass

from pyaixm.generated.notamtranslation_type import NotamtranslationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Notamtranslation(NotamtranslationType):
    class Meta:
        name = "NOTAMTranslation"
        namespace = "http://www.aixm.aero/schema/5.1/event"
