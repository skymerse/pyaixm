from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)
from pyaixm.generated.code_radio_signal_type import CodeRadioSignalType
from pyaixm.generated.code_status_navaid_type import CodeStatusNavaidType
from pyaixm.generated.navaid_operational_status_type_extension import (
    NavaidOperationalStatusTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from pyaixm.generated.timesheet_property_type import TimesheetPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidOperationalStatusType(AbstractPropertiesWithScheduleType):
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
    operational_status: Optional[CodeStatusNavaidType] = field(
        default=None,
        metadata={
            "name": "operationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    signal_type: Optional[CodeRadioSignalType] = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[NavaidOperationalStatusTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
