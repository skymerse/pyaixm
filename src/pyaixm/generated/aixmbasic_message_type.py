from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_aixmmessage_type import AbstractAixmmessageType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/message"


@dataclass
class AixmbasicMessageType(AbstractAixmmessageType):
    class Meta:
        name = "AIXMBasicMessageType"

    target_namespace_element: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "process_contents": "skip",
        },
    )
