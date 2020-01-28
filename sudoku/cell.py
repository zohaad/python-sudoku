import typing as t

class Cell:
    def __init__(self, candidates: t.List[int]=None):
        if candidates is None:
            self.candidates = list(range(1, 10))
        else:
            self.candidates = candidates.copy()

    def solved(self) -> bool:
        return len(self.candidates) == 1
