from dataclasses import dataclass

from generated.wind_direction_indicator_type import WindDirectionIndicatorType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class WindDirectionIndicator(WindDirectionIndicatorType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
