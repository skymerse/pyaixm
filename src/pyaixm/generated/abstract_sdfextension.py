from dataclasses import dataclass

from pyaixm.generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSdfextension(AbstractExtensionType):
    class Meta:
        name = "AbstractSDFExtension"
        namespace = "http://www.aixm.aero/schema/5.1"
