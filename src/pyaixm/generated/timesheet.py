from dataclasses import dataclass

from generated.timesheet_type import TimesheetType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Timesheet(TimesheetType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
