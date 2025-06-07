from dataclasses import dataclass

from pyaixm.generated.ridge_extension_type import RidgeExtensionType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RidgeExtension(RidgeExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
