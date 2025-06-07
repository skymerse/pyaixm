from dataclasses import dataclass

from pyaixm.generated.vorextension_type import VorextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Vorextension(VorextensionType):
    class Meta:
        name = "VORExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
