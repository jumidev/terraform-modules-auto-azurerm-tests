SHELL:=/bin/bash
.PHONY: venv test_venv test

venv:
	python3 -m venv venv
	(source venv/bin/activate && pip install -r requirements.txt)

test_venv:
	(source venv/bin/activate && cd tests && python3 -m pytest pytest_batch_01.py)

test:
	cd tests && python3 -m pytest pytest_batch_01.py