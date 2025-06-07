from dataclasses import dataclass

from pyaixm.generated.contact_information_type import ContactInformationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ContactInformation(ContactInformationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
