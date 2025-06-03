from dataclasses import dataclass

from generated.code_list_value_type import CodeListValueType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCellGeometryCode(CodeListValueType):
    class Meta:
        name = "MD_CellGeometryCode"
        namespace = "http://www.isotc211.org/2005/gmd"
