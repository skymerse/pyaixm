from dataclasses import dataclass

from pyaixm.generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractNdbextension(AbstractExtensionType):
    class Meta:
        name = "AbstractNDBExtension"
        namespace = "http://www.aixm.aero/schema/5.1"
