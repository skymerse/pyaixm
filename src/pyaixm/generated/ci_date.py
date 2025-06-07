from dataclasses import dataclass

from pyaixm.generated.ci_date_type import CiDateType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiDate(CiDateType):
    class Meta:
        name = "CI_Date"
        namespace = "http://www.isotc211.org/2005/gmd"
