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


fetch-products:
	flask product fetch

clear-tmp:
	rm -r tmp/*

reconcile:
	flask product insert
