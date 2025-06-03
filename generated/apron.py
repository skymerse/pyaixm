from dataclasses import dataclass

from generated.apron_type import ApronType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Apron(ApronType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
