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

## Development

Python data classes are generated from XML schema definition files from official AIXM java package found at https://github.com/faa-swim/aixm-5.1 (we use our public [fork](https://github.com/skymerse/aixm-5.1) of the abovementioned repo to ensure business continuity).

To regenerate bindings run following:

```bash
make
```
