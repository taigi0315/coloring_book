export PYTHON_VERSION=3.11.1
export VIRTUAL_ENV := .coloring_book-$(PYTHON_VERSION)
export PATH := $(VIRTUAL_ENV)/bin/:$(PATH)

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep

.PHONY: clean
clean:
	pyenv uninstall -f $(VIRTUAL_ENV)
	rm -rf $(VIRTUAL_ENV)
	rm -rf .cache
	rm -rf __pycache__
	rm -rf .pytest.cache
	rm -rf htmlcov
	find . -name "*.coverage" -exec rm -rf {} \;
	find . -name "htmlcov" -type f -delete

.PHONY: lint
lint:
	source $(VIRTUAL_ENV)/bin/activate \
	&& pushd coloring_book \
	&& flake8 --count --statistics \
	&& popd \
	&& deactivate

.PHONY: venv
venv: clean
	pyenv local ${PYTHON_VERSION} \
		&& python3 -m venv $(VIRTUAL_ENV) \
		&& source $(VIRTUAL_ENV)/bin/activate \
		&& python3 -m pip install --upgrade pip \
		&& python3 -m pip install -r requirements.txt \
