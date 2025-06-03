from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractFasdataBlockExtension(AbstractExtensionType):
    class Meta:
        name = "AbstractFASDataBlockExtension"
        namespace = "http://www.aixm.aero/schema/5.1"
