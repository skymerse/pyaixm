from dataclasses import dataclass

from pyaixm.generated.standard_level_column_type import StandardLevelColumnType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelColumn(StandardLevelColumnType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
