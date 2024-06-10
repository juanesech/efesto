.PHONY: test lint docs build-cli install

install:
	pip3 install -r requirements.txt

lint: install
	flake8 .

docs: install
	pip3 install pdoc
	pdoc --output-dir public src/utils/
	pdoc --output-dir public src/cmd/
	pdoc --output-dir public src/data_sources/

test:
	@echo "Not implemented yet"

build-cli: install
	pip3 install nuitka
	python3 -m nuitka --onefile src/cli.py
