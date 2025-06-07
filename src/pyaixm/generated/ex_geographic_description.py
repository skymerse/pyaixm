from dataclasses import dataclass

from pyaixm.generated.ex_geographic_description_type import (
    ExGeographicDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicDescription(ExGeographicDescriptionType):
    class Meta:
        name = "EX_GeographicDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
