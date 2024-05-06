.PHONY: all

all: setup test check

setup: requirements.txt
	virtualenv ../venv
	../venv/bin/pip install -r requirements.txt

test: ../venv/bin/pip
	../venv/bin/pytest

check:
	../venv/bin/pylint compare.py fibonacci.py palindrom.py square.py
	../venv/bin/pycodestyle --ignore=E203 compare.py fibonacci.py palindrom.py square.py
	../venv/bin/flake8 --ignore E203,F401,F403,F405 compare.py fibonacci.py palindrom.py square.py

demo:
	./run_demo.sh

clean:
	rm -rf __pycache__
