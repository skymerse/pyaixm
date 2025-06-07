from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_extension_type import AbstractExtensionType
from generated.code_notamclassification_base_type_value import (
    CodeNotamclassificationBaseTypeValue,
)
from generated.date_time_type import DateTimeType
from generated.text_name_type import TextNameType
from generated.text_notamtype import TextNotamtype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE"


@dataclass
class EventExtensionType(AbstractExtensionType):
    classification: Optional[
        Union[str, CodeNotamclassificationBaseTypeValue]
    ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
    account_id: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "accountId",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    xoveraccount_id: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "xoveraccountID",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    xovernotam_id: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "xovernotamID",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    airportname: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    delete_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "deleteDate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    origin_id: Optional[TextNotamtype] = field(
        default=None,
        metadata={
            "name": "originID",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    qline: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    last_updated: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    canceled: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    icao_location: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "icaoLocation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
    snowtam_country_code: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "snowtamCountryCode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
            "nillable": True,
        },
    )
