from dataclasses import dataclass

from pyaixm.generated.user_defined_csproperty_type import (
    UserDefinedCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UserDefinedCsref(UserDefinedCspropertyType):
    class Meta:
        name = "userDefinedCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
