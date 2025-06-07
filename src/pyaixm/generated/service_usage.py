from dataclasses import dataclass

from generated.service_usage_type import ServiceUsageType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ServiceUsage(ServiceUsageType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
