from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_notamtype import CodeNotamtype
from generated.code_upper_alpha_type import CodeUpperAlphaType
from generated.date_time_type import DateTimeType
from generated.date_year_type import DateYearType
from generated.no_number_type import NoNumberType
from generated.notamtranslation_property_type import (
    NotamtranslationPropertyType,
)
from generated.notamtype_extension import NotamtypeExtension
from generated.text_notamtype import TextNotamtype
from generated.unit_property_type import UnitPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Notamtype(AbstractAixmobjectType):
    class Meta:
        name = "NOTAMType"

    series: Optional[CodeUpperAlphaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    number: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    year: Optional[DateYearType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    type_value: Optional[CodeNotamtype] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    issued: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    referred_series: Optional[CodeUpperAlphaType] = field(
        default=None,
        metadata={
            "name": "referredSeries",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    referred_number: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "referredNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    referred_year: Optional[DateYearType] = field(
        default=None,
        metadata={
            "name": "referredYear",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    affected_fir: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "affectedFIR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    selection_code: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "selectionCode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    traffic: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    purpose: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    scope: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    minimum_fl: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "minimumFL",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    maximum_fl: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "maximumFL",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    coordinates: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    radius: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    location: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    effective_start: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "effectiveStart",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    effective_end: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "effectiveEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    schedule: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    text: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    lower_limit: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    upper_limit: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    publisher_nof: Optional[UnitPropertyType] = field(
        default=None,
        metadata={
            "name": "publisherNOF",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    translation: Iterable[NotamtranslationPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    extension: Iterable[NotamtypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
