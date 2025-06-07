from dataclasses import dataclass

from generated.notamtype import Notamtype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Notam(Notamtype):
    class Meta:
        name = "NOTAM"
        namespace = "http://www.aixm.aero/schema/5.1/event"
