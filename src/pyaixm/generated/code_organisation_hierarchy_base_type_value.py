from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeOrganisationHierarchyBaseTypeValue(Enum):
    MEMBER = "MEMBER"
    OWNED_BY = "OWNED_BY"
    SUPERVISED_BY = "SUPERVISED_BY"
