from dataclasses import dataclass

from pyaixm.generated.dmeextension_type import DmeextensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Dmeextension(DmeextensionType):
    class Meta:
        name = "DMEExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
