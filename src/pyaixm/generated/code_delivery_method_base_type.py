from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeDeliveryMethodBaseType(Enum):
    SELF_SERVE = "SELF_SERVE"
    MOBILE = "MOBILE"
    ALL = "ALL"
    HYDRANT = "HYDRANT"
