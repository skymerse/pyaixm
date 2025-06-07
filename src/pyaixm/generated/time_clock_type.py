from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from pyaixm.generated.string_or_ref_type import StringOrRefType
from pyaixm.generated.time_calendar_property_type import (
    TimeCalendarPropertyType,
)
from pyaixm.generated.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeClockType(TimeReferenceSystemType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "referenceTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    utc_reference: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "utcReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    date_basis: Iterable[TimeCalendarPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateBasis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
