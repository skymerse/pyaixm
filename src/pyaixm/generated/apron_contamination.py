from dataclasses import dataclass

from pyaixm.generated.apron_contamination_type import ApronContaminationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronContamination(ApronContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
