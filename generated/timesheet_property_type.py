from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.timesheet import Timesheet

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TimesheetPropertyType(AbstractAixmpropertyType):
    timesheet: Optional[Timesheet] = field(
        default=None,
        metadata={
            "name": "Timesheet",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
