import sys
import os

src_root = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "pyaixm"
)
sys.path.append(src_root)

from pyaixm.aixm_message import AixmMessage
from pytest import fixture
from pyaixm import generated


@fixture
def message_a():
    with open("test/fixtures/message_a.xml", "r") as file:
        return file.read()


@fixture
def error_test_case_dme():
    with open("test/fixtures/error_test_case_dme.xml", "r") as file:
        return file.read()


def test_parse_message_a(message_a: str):
    message = AixmMessage.from_string(message_a)
    event: generated.Event = message.of_type(generated.Event)[0]

    assert (
        event.time_slice[0]
        .event_time_slice.valid_time.time_period.begin_position.value.to_datetime()
        .isoformat()
        == "2024-05-07T17:29:00+00:00"
    )


def test_parse_error_test_case_dme(error_test_case_dme: str):
    message = AixmMessage.from_string(error_test_case_dme)

    assert len(message.of_type(generated.Dme)), 1
