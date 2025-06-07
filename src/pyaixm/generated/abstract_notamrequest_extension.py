from dataclasses import dataclass

from pyaixm.generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AbstractNotamrequestExtension(AbstractExtensionType):
    class Meta:
        name = "AbstractNOTAMRequestExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
