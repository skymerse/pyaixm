from dataclasses import dataclass

from pyaixm.generated.work_area_type import WorkAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkArea(WorkAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
