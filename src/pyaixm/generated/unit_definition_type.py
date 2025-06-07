from dataclasses import dataclass, field
from typing import Optional

from generated.catalog_symbol import CatalogSymbol
from generated.definition_type import DefinitionType
from generated.quantity_type import QuantityType
from generated.quantity_type_reference import QuantityTypeReference

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UnitDefinitionType(DefinitionType):
    quantity_type: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_type_reference: Optional[QuantityTypeReference] = field(
        default=None,
        metadata={
            "name": "quantityTypeReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    catalog_symbol: Optional[CatalogSymbol] = field(
        default=None,
        metadata={
            "name": "catalogSymbol",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
