#!/bin/bash

isort src/data.py src/run.py src/utils.py src/adjust_audio_volume.py src/data_py_maker.py
black src/data.py src/run.py src/utils.py src/adjust_audio_volume.py src/data_py_maker.py
flake8 src/data.py src/run.py src/utils.py src/adjust_audio_volume.py src/data_py_maker.py
mypy src/data.py src/run.py src/utils.py src/adjust_audio_volume.py src/data_py_maker.py
