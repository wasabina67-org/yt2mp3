#!/bin/bash

isort src/data.py src/run.py
black src/data.py src/run.py
flake8 src/data.py src/run.py
mypy src/data.py src/run.py
