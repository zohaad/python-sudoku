# Sudoku solver project

This project is me trying to learn project structure in python and maybe some web stuff later on...

## Notes for myself

project structure

```
sudoku
├── README.md
├── Sports_Scheduling_Sudoku-Second_Year_Project_2017.pdf
├── setup.py
├── sudoku
│   ├── __init__.py
│   └── __main__.py
└── tests
    ├── resources
    │   ├── Sudoku1.txt
    │   ├── Sudoku2.txt
    │   ├── Sudoku3.txt
    │   ├── Sudoku4.txt
    │   ├── Sudoku5.txt
    │   └── Sudoku6.txt
    └── test_sudoku.py
```
Create the virtualenv:

`python -m venv ~/Cache/virtualenvs/sudoku-venv`

Add to path:
`source ~/Cache/virtualenvs/sudoku-venv/bin/activate`

Install the package:
`~/Cache/virtualenvs/sudoku-venv/bin/pip install -e ~/Projects/sudoku`

(-e is "editable")

Then execute:
`sudoku`