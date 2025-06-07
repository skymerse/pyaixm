from dataclasses import dataclass

from pyaixm.generated.ex_geographic_bounding_box_type import (
    ExGeographicBoundingBoxType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicBoundingBox(ExGeographicBoundingBoxType):
    class Meta:
        name = "EX_GeographicBoundingBox"
        namespace = "http://www.isotc211.org/2005/gmd"
