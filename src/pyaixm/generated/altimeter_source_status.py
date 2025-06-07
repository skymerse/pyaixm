from dataclasses import dataclass

from generated.altimeter_source_status_type import AltimeterSourceStatusType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSourceStatus(AltimeterSourceStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
