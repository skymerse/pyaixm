from dataclasses import dataclass

from generated.code_or_nil_reason_list_type import CodeOrNilReasonListType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CategoryList(CodeOrNilReasonListType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
