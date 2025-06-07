from dataclasses import dataclass

from pyaixm.generated.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopologyLevelCode(CodeListValueType):
    class Meta:
        name = "MD_TopologyLevelCode"
        namespace = "http://www.isotc211.org/2005/gmd"
