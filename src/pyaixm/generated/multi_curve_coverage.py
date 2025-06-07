from dataclasses import dataclass

from generated.discrete_coverage_type import DiscreteCoverageType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveCoverage(DiscreteCoverageType):
    """In a gml:MultiCurveCoverage the domain is partioned into a collection of
    curves comprising a gml:MultiCurve.  The coverage function then maps each curve
    in the collection to a value in the range set. The content model is identical
    with gml:DiscreteCoverageType, but that gml:domainSet shall have values
    gml:MultiCurve.

    In a gml:MultiCurveCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the curves of the gml:MultiCurve are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the curves of the gml:MultiCurve are mapped to the members of the composite value in document order.
    -       For gml:File encodings the curves of the gml:MultiCurve are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
