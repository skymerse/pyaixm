from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.md_identifier_type import CiCitationPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReferenceType(AbstractObjectType):
    """
    Information identifing the portrayal catalogue used.
    """

    class Meta:
        name = "MD_PortrayalCatalogueReference_Type"

    portrayal_catalogue_citation: Iterable[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
