from dataclasses import dataclass

from pyaixm.generated.ais_publication_type import AisPublicationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AisPublication(AisPublicationType):
    class Meta:
        name = "AIS_Publication"
        namespace = "http://www.aixm.aero/schema/5.1/event"
