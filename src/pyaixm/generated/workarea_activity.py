from dataclasses import dataclass

from pyaixm.generated.workarea_activity_type import WorkareaActivityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkareaActivity(WorkareaActivityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
