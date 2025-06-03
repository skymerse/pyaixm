from dataclasses import dataclass

from generated.telephone_contact_type import TelephoneContactType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TelephoneContact(TelephoneContactType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
