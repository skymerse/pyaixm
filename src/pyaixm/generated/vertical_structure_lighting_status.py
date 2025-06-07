from dataclasses import dataclass

from generated.vertical_structure_lighting_status_type import (
    VerticalStructureLightingStatusType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureLightingStatus(VerticalStructureLightingStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
