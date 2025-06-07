from dataclasses import dataclass

from pyaixm.generated.abstract_time_primitive_type import (
    TimePrimitivePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FeatureLifetime(TimePrimitivePropertyType):
    """The start and end of life of the feature.

    See the AIXM Temporality model for details.
    """

    class Meta:
        name = "featureLifetime"
        namespace = "http://www.aixm.aero/schema/5.1"
