from dataclasses import dataclass

from pyaixm.generated.code_type import CodeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScopedName(CodeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
