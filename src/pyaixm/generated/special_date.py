from dataclasses import dataclass

from pyaixm.generated.special_date_type import SpecialDateType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialDate(SpecialDateType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
