from dataclasses import dataclass

from pyaixm.generated.work_area_extension_type import WorkAreaExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class WorkAreaExtension(WorkAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
