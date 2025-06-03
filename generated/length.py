from dataclasses import dataclass

from generated.length_type import LengthType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Length(LengthType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
