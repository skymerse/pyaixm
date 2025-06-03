from dataclasses import dataclass

from generated.abstract_extension_type import AbstractExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AbstractAisPublicationExtension(AbstractExtensionType):
    class Meta:
        name = "AbstractAIS_PublicationExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
