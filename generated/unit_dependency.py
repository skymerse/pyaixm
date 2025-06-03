from dataclasses import dataclass

from generated.unit_dependency_type import UnitDependencyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitDependency(UnitDependencyType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
