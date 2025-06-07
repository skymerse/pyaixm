from dataclasses import dataclass

from generated.arresting_gear_extension_type import ArrestingGearExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ArrestingGearExtension(ArrestingGearExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
