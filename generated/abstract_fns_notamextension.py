from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AbstractFnsNotamextension(AbstractExtensionType):
    class Meta:
        name = "AbstractFNS_NOTAMExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
