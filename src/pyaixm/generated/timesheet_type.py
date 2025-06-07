from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_day_type import CodeDayType
from generated.code_time_event_combination_type import (
    CodeTimeEventCombinationType,
)
from generated.code_time_event_type import CodeTimeEventType
from generated.code_time_reference_type import CodeTimeReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.date_month_day_type import DateMonthDayType
from generated.note_property_type import NotePropertyType
from generated.time_type_2 import TimeType2
from generated.timesheet_type_extension import TimesheetTypeExtension
from generated.val_duration_type import ValDurationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TimesheetType(AbstractAixmobjectType):
    time_reference: Optional[CodeTimeReferenceType] = field(
        default=None,
        metadata={
            "name": "timeReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    day: Optional[CodeDayType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    day_til: Optional[CodeDayType] = field(
        default=None,
        metadata={
            "name": "dayTil",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_time: Optional[TimeType2] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_event: Optional[CodeTimeEventType] = field(
        default=None,
        metadata={
            "name": "startEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_time_relative_event: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "name": "startTimeRelativeEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_event_interpretation: Optional[CodeTimeEventCombinationType] = field(
        default=None,
        metadata={
            "name": "startEventInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_time: Optional[TimeType2] = field(
        default=None,
        metadata={
            "name": "endTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_event: Optional[CodeTimeEventType] = field(
        default=None,
        metadata={
            "name": "endEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_time_relative_event: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "name": "endTimeRelativeEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_event_interpretation: Optional[CodeTimeEventCombinationType] = field(
        default=None,
        metadata={
            "name": "endEventInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    daylight_saving_adjust: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "daylightSavingAdjust",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    excluded: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TimesheetTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
