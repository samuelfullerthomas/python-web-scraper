.PHONY: bootstrap start

bootstrap:
	pipenv install

start:
	python3 scraper.py