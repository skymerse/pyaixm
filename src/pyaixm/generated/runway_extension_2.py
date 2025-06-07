from dataclasses import dataclass

from generated.runway_extension_type_2 import RunwayExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayExtension2(RunwayExtensionType2):
    class Meta:
        name = "RunwayExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
