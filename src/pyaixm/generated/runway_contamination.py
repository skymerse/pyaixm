from dataclasses import dataclass

from pyaixm.generated.runway_contamination_type import RunwayContaminationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayContamination(RunwayContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
