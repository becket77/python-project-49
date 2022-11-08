install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

flake8:
	poetry add --group dev flake8

make lint:
	poetry run flake8 brain_games
