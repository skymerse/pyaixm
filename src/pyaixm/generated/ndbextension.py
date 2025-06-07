from dataclasses import dataclass

from generated.ndbextension_type import NdbextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Ndbextension(NdbextensionType):
    class Meta:
        name = "NDBExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
