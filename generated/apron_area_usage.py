from dataclasses import dataclass

from generated.apron_area_usage_type import ApronAreaUsageType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronAreaUsage(ApronAreaUsageType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
