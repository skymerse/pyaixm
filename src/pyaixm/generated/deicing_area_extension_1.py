from dataclasses import dataclass

from generated.deicing_area_extension_type_1 import DeicingAreaExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DeicingAreaExtension1(DeicingAreaExtensionType1):
    class Meta:
        name = "DeicingAreaExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
