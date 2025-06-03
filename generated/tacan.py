from dataclasses import dataclass

from generated.tacantype import Tacantype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Tacan(Tacantype):
    class Meta:
        name = "TACAN"
        namespace = "http://www.aixm.aero/schema/5.1"
