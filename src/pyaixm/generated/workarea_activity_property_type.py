from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.workarea_activity import WorkareaActivity

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkareaActivityPropertyType(AbstractAixmpropertyType):
    workarea_activity: Optional[WorkareaActivity] = field(
        default=None,
        metadata={
            "name": "WorkareaActivity",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
