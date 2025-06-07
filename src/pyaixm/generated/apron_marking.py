from dataclasses import dataclass

from pyaixm.generated.apron_marking_type import ApronMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronMarking(ApronMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
