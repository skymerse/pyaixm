from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.ais_publication_type_extension import (
    AisPublicationTypeExtension,
)
from generated.code_aispublication_type import CodeAispublicationType
from generated.code_upper_alpha_type import CodeUpperAlphaType
from generated.date_time_type import DateTimeType
from generated.date_year_type import DateYearType
from generated.no_number_type import NoNumberType
from generated.unit_property_type import UnitPropertyType
from generated.xhtmltype import Xhtmltype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AisPublicationType(AbstractAixmobjectType):
    class Meta:
        name = "AIS_PublicationType"

    type_value: Optional[CodeAispublicationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
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
    issued: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    effective_start: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "effectiveStart",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    effective_end: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "effectiveEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    content: Optional[Xhtmltype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    publisher: Optional[UnitPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    extension: Iterable[AisPublicationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
