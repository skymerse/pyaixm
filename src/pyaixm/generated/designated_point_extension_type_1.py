from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.event_property_type import EventPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DesignatedPointExtensionType1(AbstractExtensionType):
    class Meta:
        name = "DesignatedPointExtensionType"

    the_event: Iterable[EventPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "theEvent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "nillable": True,
        },
    )
