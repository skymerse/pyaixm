from dataclasses import dataclass

from generated.online_contact_type import OnlineContactType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OnlineContact(OnlineContactType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
