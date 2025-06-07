from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AbstractServiceUsageExtension(AbstractExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
