from dataclasses import dataclass

from generated.runway_extension_type_1 import RunwayExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayExtension1(RunwayExtensionType1):
    class Meta:
        name = "RunwayExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
