from dataclasses import dataclass

from pyaixm.generated.multiplicity_range_type import MultiplicityRangeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityRange(MultiplicityRangeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
