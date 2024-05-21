# LLM-MCQ-Generator

Create a virtual environment for your application using python

1. python -m venv env
2. cd env/Scripts
3. activate(use .\activate if activate does not work)

Create a virtual environment for your application using anaconda

1. conda create -p env python=<python_version_name> -y
2. source activate ./env

## Notes and Learnings

This section contains the extra information and notes you want to retain.

### Learnings

- **setup.py**: This file contains metadata related to the project which contains project name,author,author name,author email,etc.
- **find_packages()**: This method will discover all the local packages in the project directory.
- **init.py**: This file is used to create a local package for a directory.
- To install all the packages we use pip install -r requirements.txt
- To install the local packages in the virtual environment use -e .
