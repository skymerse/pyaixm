from dataclasses import dataclass

from generated.md_reference_system_type import MdReferenceSystemType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdReferenceSystem(MdReferenceSystemType):
    class Meta:
        name = "MD_ReferenceSystem"
        namespace = "http://www.isotc211.org/2005/gmd"
