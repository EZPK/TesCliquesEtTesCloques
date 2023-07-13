.Phony: help
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install
install: venv/bin/pip
	venv/bin/pip install -r requirement.txt
	venv/bin/python3 main.py

.PHONY: clean
clean:
	rm -rf venv
	ls -la

venv/bin/pip:
	python3 -m venv venv