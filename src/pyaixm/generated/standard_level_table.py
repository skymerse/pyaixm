from dataclasses import dataclass

from pyaixm.generated.standard_level_table_type import StandardLevelTableType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelTable(StandardLevelTableType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
