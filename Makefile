SHELL:=/bin/bash
.PHONY: venv test_venv test

venv:
	python3 -m venv venv
	(source venv/bin/activate && pip install -r requirements.txt)

test_venv:
	(source venv/bin/activate && bash -x runtests.sh)

test:
	bash -x runtests.sh