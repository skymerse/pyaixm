from dataclasses import dataclass

from pyaixm.generated.member_name_type import MemberNameType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MemberName(MemberNameType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
