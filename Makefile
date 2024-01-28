# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init::
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	flask run

black:
	black .

black-check:
	black --check .

flake8:
	flake8 --exclude .venv,node_modules

isort:
	isort --profile black .

db-migration:
	flask db migrate

db-upgrade:
	flask db upgrade


flask:
	flask run

fetch-products:
	flask product fetch

tmp:
	mkdir tmp

clear-tmp:
	rm -r tmp/*

reconcile:
	flask product insert

latest-prices:
	flask price latest

status:
	git status --ignored

commit-products::
	git add .
	git diff --quiet && git diff --staged --quiet || (git commit -m "Latest product details $(shell date +%F)"; git push origin $(BRANCH))
