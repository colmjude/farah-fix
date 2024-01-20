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
