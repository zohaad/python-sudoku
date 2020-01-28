import typing as t
from sudoku.cell import Cell

class Sudoku:
    def __init__(self):
        self.matrix = self.get_new_matrix()
    
    def get_new_matrix(self) -> t.List[t.List[Cell]]:
        return [[Cell() for _ in range(9)] for _ in range(9)]