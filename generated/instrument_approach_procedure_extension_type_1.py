from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_extension_type import AbstractExtensionType
from generated.event_property_type import EventPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class InstrumentApproachProcedureExtensionType1(AbstractExtensionType):
    class Meta:
        name = "InstrumentApproachProcedureExtensionType"

    the_event: Iterable[EventPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "theEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
