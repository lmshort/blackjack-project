## Introduction
CLI Blackjack game project

## Set up

This project uses Poetry for packaging and dependency management (https://python-poetry.org/).
- Download and activate python 3.8
- Run `poetry init` in the root directory - this will create the venv and install the dependencies listed in the pyproject.TOML
- Enable the pre-commit hooks, integrating with Git by running `pre-commit install`

## Running the Game

- Execute the main.py file from within the venv. This file is located within: ~/blackjack_project/
- To exit the game, either quit debugging from within an IDE, or from the terminal use Ctrl+Z to escape.

## Tests

- Tests are located within the tests directory
- To execute all tests, execute the run_tests.sh bash script

## Reformatting

- To manually reformat all existing scripts, execute the reformat_all.sh bash script found within ~/blackjack_project/

## Committing code

- The pre-commit-config uses Black to automatically fix simple formatting issues when commiting.
- Unit tests are executed automatically when commiting code.
