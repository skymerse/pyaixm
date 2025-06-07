from dataclasses import dataclass

from pyaixm.generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AbstractNotamextension(AbstractExtensionType):
    class Meta:
        name = "AbstractNOTAMExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
