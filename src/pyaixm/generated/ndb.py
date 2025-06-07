from dataclasses import dataclass

from generated.ndbtype import Ndbtype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Ndb(Ndbtype):
    class Meta:
        name = "NDB"
        namespace = "http://www.aixm.aero/schema/5.1"
