# behqtcsdl

## Setup, Run, Test

- Install python version 3.9, prefer [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) for environment switch.
- Install [poetry](https://github.com/python-poetry/poetry).
- Install [pre-commit](https://pre-commit.com/).
- copy .env.txt and rename to .env (change env inside to fit your local env).

```bash
# install pre-commit in projects
$ pre-commit install


# install dependencies
$ cd ./services/src && poetry install

# run local development with reload
$ poetry run uvicorn app.main:app --reload

# add new dependency
poetry add --dev <package>
poetry add <package>

# run tests
$ poetry run pytest app/tests/integration/

# run local check
poetry run black . --check
poetry run isort . --check-only --profile black
poetry run flake8 .
poetry run bandit .
poetry run safety check

# export deps if changes
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
