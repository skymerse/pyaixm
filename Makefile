.PHONY: generate

generate:
	rm -rf generated/
	uv run xsdata generate --generic-collections --config xsdata.xml aixm-5.1/src/main/fns2.0_xsds/

tests:
	uv run pytest
	
