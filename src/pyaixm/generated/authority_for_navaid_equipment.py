from dataclasses import dataclass

from generated.authority_for_navaid_equipment_type import (
    AuthorityForNavaidEquipmentType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForNavaidEquipment(AuthorityForNavaidEquipmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
