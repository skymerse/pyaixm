from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_notamstatus_type import CodeNotamstatusType
from pyaixm.generated.date_month_day_type import DateMonthDayType
from pyaixm.generated.fns_notamtype_extension import FnsNotamtypeExtension

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FnsNotamtype(AbstractAixmobjectType):
    class Meta:
        name = "FNS_NOTAMType"

    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionID",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    status: Optional[CodeNotamstatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    accountability: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "pattern": r"([A-Z]|\d)*",
        },
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "pattern": r"([A-Z]|\d)*",
        },
    )
    notam_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "notamID",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    issued_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "issuedDate",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cancelled_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "cancelledDate",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    start_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    end_date: Optional[DateMonthDayType] = field(
        default=None,
        metadata={
            "name": "endDate",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    condition_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "conditionText",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    us_notamtext: Optional[str] = field(
        default=None,
        metadata={
            "name": "usNOTAMText",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    icao_notamtext: Optional[str] = field(
        default=None,
        metadata={
            "name": "icaoNOTAMText",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    plain_notamtext: Optional[str] = field(
        default=None,
        metadata={
            "name": "plainNOTAMText",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    extension: Iterable[FnsNotamtypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
