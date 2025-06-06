from aixm_message import AixmMessage
from pytest import fixture
import generated


@fixture
def message_a():
    with open("test/fixtures/message_a.xml", "r") as file:
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
