from dataclasses import dataclass

from pyaixm.generated.fns_notamtype import FnsNotamtype

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class FnsNotam(FnsNotamtype):
    class Meta:
        name = "FNS_NOTAM"
        namespace = "urn:us.gov.dot.faa.aim.fns"
