flake8:
	@flake8 --config config/tox.ini

test:
	@poetry run pytest

requirements:
	@poetry export -f requirements.txt --output requirements.txt --without-hashes

dev_requirements:
	@poetry export --with dev -f requirements.txt --output requirements_dev.txt

version:
	@make flake8
	@make test
	@make requirements
	@git add .
	@git commit -m "v$$(poetry version -s)"
	@git tag v$$(poetry version -s)
	@git push
	@git push --tags
	@poetry version

