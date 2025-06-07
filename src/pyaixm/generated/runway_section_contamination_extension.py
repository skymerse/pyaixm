from dataclasses import dataclass

from generated.runway_section_contamination_extension_type import (
    RunwaySectionContaminationExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwaySectionContaminationExtension(
    RunwaySectionContaminationExtensionType
):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
