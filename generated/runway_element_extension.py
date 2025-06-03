from dataclasses import dataclass

from generated.runway_element_extension_type import RunwayElementExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayElementExtension(RunwayElementExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
