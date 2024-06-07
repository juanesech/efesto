lint:
	flake8 .

docs:
	pip install pdoc
	pdoc --docformat markdown --output-dir ../../public src/data_sources/
	pdoc --docformat markdown --output-dir ../../public src/utils/
	pdoc --docformat markdown --output-dir ../../public src/cmd/

test:
	@echo "Not implemented yet"
	#pytest
