from dataclasses import dataclass

from generated.postal_address_type import PostalAddressType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PostalAddress(PostalAddressType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
