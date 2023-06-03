import pytest

from main import my_sum


def test_my_sum():
    assert my_sum(2, 3) == 5


def test_my_sum_zero():
    assert my_sum(1, 0) == 1



'''
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
-   repo: https://github.com/PyCQA/isort
    rev: 5.9.3
    hooks:
        - id: isort
-   repo: https://github.com/PyCQA/flake8
    rev: 3.9.2
    hooks:
        - id: flake8
-   repo: local
    hooks:
        - id: pytest
          name: pytest
          entry: pytest
          language: system
          always_run: true
          verbose: true
          pass_filenames: false
'''
