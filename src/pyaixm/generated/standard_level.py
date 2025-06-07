from dataclasses import dataclass

from pyaixm.generated.standard_level_type import StandardLevelType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevel(StandardLevelType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
