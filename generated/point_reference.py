from dataclasses import dataclass

from generated.point_reference_type import PointReferenceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PointReference(PointReferenceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
