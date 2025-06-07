from dataclasses import dataclass

from pyaixm.generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractProcedureDmeextension(AbstractExtensionType):
    class Meta:
        name = "AbstractProcedureDMEExtension"
        namespace = "http://www.aixm.aero/schema/5.1"
