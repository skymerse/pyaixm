from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.ais_publication_property_type import (
    AisPublicationPropertyType,
)
from pyaixm.generated.code_event_encoding_type import CodeEventEncodingType
from pyaixm.generated.date_time_type import DateTimeType
from pyaixm.generated.event_property_type import EventPropertyType
from pyaixm.generated.event_time_slice_type_extension import (
    EventTimeSliceTypeExtension,
)
from pyaixm.generated.notamproperty_type import NotampropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_designator_type import TextDesignatorType
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class EventTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    encoding: Optional[CodeEventEncodingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    scenario: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    revision: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    text_notam: Iterable[NotampropertyType] = field(
        default_factory=list,
        metadata={
            "name": "textNOTAM",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    cause_event: Optional[EventPropertyType] = field(
        default=None,
        metadata={
            "name": "causeEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    the_note: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "theNote",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    document_ais: Iterable[AisPublicationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "documentAIS",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
    extension: Iterable[EventTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
