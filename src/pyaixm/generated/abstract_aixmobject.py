from dataclasses import dataclass

from generated.abstract_aixmobject_type import AbstractAixmobjectType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmobject(AbstractAixmobjectType):
    """
    Substitution head for AIXM objects.
    """

    class Meta:
        name = "AbstractAIXMObject"
        namespace = "http://www.aixm.aero/schema/5.1"
