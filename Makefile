.PHONY: generate

generate:
	rm -rf src/pyaixm/generated/
	uv run xsdata generate --generic-collections --config xsdata.xml aixm-5.1/src/main/fns2.0_xsds/
	mv pyaixm/generated src/pyaixm/
	rm -rf pyaixm/


tests:
	uv run pytest
	
