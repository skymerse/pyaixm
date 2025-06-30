# PyAIXM

[AIXM](https://aixm.aero/) python bindings.

## Installation

### Using pip

```bash
pip install git+https://github.com/skymerse/pyaixm.git
```

### Using uv

```bash
uv add git+https://github.com/skymerse/pyaixm.git
```

## Usage

PyAIXM provides a convenient way to parse and work with AIXM XML messages. Here's how to use it:

### Basic Usage

```python
from pyaixm import AixmMessage
from pyaixm.generated import (
    Event,
    EventTimeSlice,
    Notam,
)

# Parse an AIXM XML message
xml_content = "..." # see test/fixtures/message_a.xml for reference

# Parse the XML message
message = AixmMessage.from_string(xml_content)

# Iterate over all members
for member in message:
    print(f"Member type: {type(member).__name__}")

# Filter members by type
events = message.of_type(Event)

# Extract data from Event member
event = events[0]

event_time_slice: EventTimeSlice = event.time_slice[0]
ets = getattr(event_time_slice, "event_time_slice", None)
text_notam = getattr(ets, "text_notam", None) if ets else None
notam = text_notam[0].notam

# Extract start and end times
start_time = ets.valid_time.time_period.begin_position.value.to_datetime()
```

### Working with Different AIXM Features

The library supports all AIXM 5.1 features. Here are some common examples:

```python
# Filter for different types of features
airports = message.of_type(generated.AirportHeliport)
airspaces = message.of_type(generated.Airspace)
runways = message.of_type(generated.Runway)
waypoints = message.of_type(generated.Waypoint)

# Access time slice data
for airport in airports:
    for time_slice in airport.time_slice:
        print(f"Airport: {time_slice.name}")
        print(f"Interpretation: {time_slice.interpretation}")
        
        # Access availability information
        if time_slice.availability:
            for availability in time_slice.availability:
                print(f"Status: {availability.status}")
```

### Error Handling

The parser includes error recovery for malformed XML:

```python
try:
    message = AixmMessage.from_string(xml_content)
    print(f"Successfully parsed {len(message)} members")
except Exception as e:
    print(f"Error parsing XML: {e}")
```

## Development

Python data classes are generated from XML schema definition files from official AIXM java package found at https://github.com/faa-swim/aixm-5.1 (we use our public [fork](https://github.com/skymerse/aixm-5.1) of the abovementioned repo to ensure business continuity).

To regenerate bindings run following:

```bash
make
```
