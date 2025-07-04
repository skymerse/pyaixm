from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
import pyaixm.generated as generated
from typing import Any
import sys
import inflection


def _feature_name_variants(feature_name: str) -> list[str]:
    """
    Returns a list of possible variants of the feature name, i.e.
    - feature name as is
    - feature name in UpperCamelCase
    """
    return [
        feature_name,
        inflection.camelize(feature_name, uppercase_first_letter=True),
        inflection.camelize(feature_name.lower(), uppercase_first_letter=True),
    ]


class AixmMessage:
    """
    A thin wrapper around the AixmBasicMessage class.
    It provides a convenient way to parse and iterate over the members of the message.
    """

    def __init__(self, members: list[Any]):
        self.members = members

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index: int):
        return self.members[index]

    def of_type(self, clazz: Any):
        return [member for member in self.members if isinstance(member, clazz)]

    @staticmethod
    def from_string(xml_content: str):
        tree = etree.fromstring(
            xml_content.encode("utf-8"),
            parser=etree.XMLParser(recover=True),
        )
        # Get all hasMember nodes
        has_members = tree.findall(
            ".//{http://www.aixm.aero/schema/5.1/message}hasMember"
        )

        parser = XmlParser()
        # Extract raw XML for each member
        members = []
        for member in has_members:
            # Get the first child element of hasMember
            child = member[0]

            feature_name = None
            feature_name_variants = _feature_name_variants(child.tag.split("}")[-1])
            for feature_name_variant in feature_name_variants:
                if hasattr(generated, feature_name_variant):
                    feature_name = feature_name_variant
                    break

            if (feature_name is None):
                print(f"Warning: Feature '{feature_name_variant}' not found in generated classes", file=sys.stderr)
                continue

            feature_class = getattr(generated, feature_name)

            # Convert to string
            member_xml = etree.tostring(child, encoding="unicode")
            feature = parser.from_string(member_xml, feature_class)
            members.append(feature)

        return AixmMessage(members)
