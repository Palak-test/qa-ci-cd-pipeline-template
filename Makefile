# ContainerLabPy Build

This Makefile will provide build and test commands for the project.

install:
	pip install -e .

test:
	python -m unittest discover core/tests
