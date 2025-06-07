from dataclasses import dataclass

from pyaixm.generated.runway_section_contamination_type import (
    RunwaySectionContaminationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwaySectionContamination(RunwaySectionContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
