# PyAIXM

AIXM python bindings. 

## Development

Python data classes are generated from XML schema definition files from official AIXM java package found at https://github.com/faa-swim/aixm-5.1 (we use our public fork of the abovementioned repo to ensure business continuity).

To regenerate bindings run following:

```bash
make
```
