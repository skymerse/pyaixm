from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractTerminalArrivalAreaExtension(AbstractExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
