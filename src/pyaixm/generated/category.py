from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_type import CodeType
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Category(CodeType):
    """
    A gml:Category has an optional XML attribute codeSpace, whose value is a URI
    which identifies a dictionary, codelist or authority for the term.
    """

    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
