from dataclasses import dataclass

from pyaixm.generated.unit_extension_type import UnitExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class UnitExtension(UnitExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
