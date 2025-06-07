from dataclasses import dataclass

from generated.manoeuvring_area_usage_type import ManoeuvringAreaUsageType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaUsage(ManoeuvringAreaUsageType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
