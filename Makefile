# Pas fonctionnel sous windows

.Phony: help
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install
install: venv/lib/pip
	venv/lib/pip install -r ./requirements.txt
	venv/lib/python main.py

.PHONY: clean
clean:
	rm -rf venv
	ls -la

venv/lib/pip:
	python -m venv venv