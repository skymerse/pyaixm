from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractDmeextension(AbstractExtensionType):
    class Meta:
        name = "AbstractDMEExtension"
        namespace = "http://www.aixm.aero/schema/5.1"
