from dataclasses import dataclass

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmfeature(AbstractAixmfeatureType):
    """
    Substitution head for AIXM features.
    """

    class Meta:
        name = "AbstractAIXMFeature"
        namespace = "http://www.aixm.aero/schema/5.1"
