from dataclasses import dataclass

from pyaixm.generated.tacanextension_type import TacanextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Tacanextension(TacanextensionType):
    class Meta:
        name = "TACANExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
