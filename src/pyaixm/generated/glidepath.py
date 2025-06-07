from dataclasses import dataclass

from pyaixm.generated.glidepath_type import GlidepathType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Glidepath(GlidepathType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
