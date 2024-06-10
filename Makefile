.PHONY: test lint docs build-cli
lint:
	flake8 .

docs:
	pip3 install pdoc
	pdoc --output-dir public src/utils/
	pdoc --output-dir public src/cmd/
	pdoc --output-dir public src/data_sources/

test:
	@echo "Not implemented yet"

build-cli:
	pip3 install nuitka
	python3 -m nuitka --onefile src/cli.py


