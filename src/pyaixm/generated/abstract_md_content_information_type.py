from dataclasses import dataclass

from pyaixm.generated.abstract_object_type import AbstractObjectType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdContentInformationType(AbstractObjectType):
    class Meta:
        name = "AbstractMD_ContentInformation_Type"
