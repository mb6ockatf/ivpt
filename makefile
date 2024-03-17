#!/usr/bin/make -f

setup_dev:
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -r requirements.txt
