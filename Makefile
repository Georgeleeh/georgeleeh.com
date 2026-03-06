SHELL := /bin/bash

.PHONY: init requirements run test build start stop

init:
	rm -rf .venv
	python3 -m venv .venv

requirements:
	source .venv/bin/activate && pip install -r requirements.txt

run:
	source .venv/bin/activate && flask --app app.py run

test:
	echo "No tests yet"

build:
	docker build -t georgeleeh-portfolio .

start:
	docker run --name georgeleeh-portfolio -d -p 5000:5000 georgeleeh-portfolio

stop:
	docker stop georgeleeh-portfolio && docker rm georgeleeh-portfolio
