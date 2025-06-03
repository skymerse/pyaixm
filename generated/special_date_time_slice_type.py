from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_special_date_type import CodeSpecialDateType
from generated.date_month_day_type import DateMonthDayType
from generated.date_year_type import DateYearType
from generated.note_property_type import NotePropertyType
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from generated.special_date_time_slice_type_extension import (
    SpecialDateTimeSliceTypeExtension,
)
from generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialDateTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeSpecialDateType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    date_day: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "dateDay",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    date_year: Optional[DateYearType] = field(
        default=None,
        metadata={
            "name": "dateYear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    name: Optional[TextNameType] = field(
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
    authority: Optional[OrganisationAuthorityPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[SpecialDateTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
