from dataclasses import dataclass

from pyaixm.generated.aixmbasic_message_type import AixmbasicMessageType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/message"


@dataclass
class AixmbasicMessage(AixmbasicMessageType):
    class Meta:
        name = "AIXMBasicMessage"
        namespace = "http://www.aixm.aero/schema/5.1/message"
