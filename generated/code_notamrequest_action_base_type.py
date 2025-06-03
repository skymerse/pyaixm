from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeNotamrequestActionBaseType(Enum):
    CREATE_NOTAM = "CREATE_NOTAM"
    CANCEL_NOTAM = "CANCEL_NOTAM"
    CHECK_NOTAM_STATUS = "CHECK_NOTAM_STATUS"
    CREATE_NOTAM_PREVIEW = "CREATE_NOTAM_PREVIEW"
