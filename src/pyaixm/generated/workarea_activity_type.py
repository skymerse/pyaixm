from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from generated.code_yes_no_type import CodeYesNoType
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from generated.timesheet_property_type import TimesheetPropertyType
from generated.workarea_activity_type_extension import (
    WorkareaActivityTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkareaActivityType(AbstractPropertiesWithScheduleType):
    time_interval: Iterable[TimesheetPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeInterval",
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
    special_date_authority: Iterable[OrganisationAuthorityPropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "specialDateAuthority",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    is_active: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "isActive",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[WorkareaActivityTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
