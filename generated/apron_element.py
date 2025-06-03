from dataclasses import dataclass

from generated.apron_element_type import ApronElementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronElement(ApronElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
