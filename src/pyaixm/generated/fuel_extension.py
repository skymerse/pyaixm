from dataclasses import dataclass

from pyaixm.generated.fuel_extension_type import FuelExtensionType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FuelExtension(FuelExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
