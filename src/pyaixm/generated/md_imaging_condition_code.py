from dataclasses import dataclass

from pyaixm.generated.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImagingConditionCode(CodeListValueType):
    class Meta:
        name = "MD_ImagingConditionCode"
        namespace = "http://www.isotc211.org/2005/gmd"
