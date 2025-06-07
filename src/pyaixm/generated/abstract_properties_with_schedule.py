from dataclasses import dataclass

from pyaixm.generated.abstract_properties_with_schedule_type import (
    AbstractPropertiesWithScheduleType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractPropertiesWithSchedule(AbstractPropertiesWithScheduleType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
