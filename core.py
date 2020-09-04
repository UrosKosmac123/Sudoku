
def getBlockIndices(block):
    x = (block % 3) * 3
    y = (block // 3) * 3
    return [[x + i % 3, y + i // 3] for i in range(9)]

"""
Stanje sudoku aplikacije.
"""
class State:

    """
    Konstruktor stanja, ki inicializira novo prazno matriko.
    """
    def __init__(self):
        self.matrix = [[None for y in range(9)] for x in range(9)]
        self.locked = [[False for y in range(9)] for x in range(9)]

    """
    Izpis stanja v berljivi obliki.
    """
    def __str__(self):
        return "\n".join(
            [
                " ".join([str(v) if v is not None else "-" for v in col])
                for col in self.matrix
            ]
        )

    """
    Klonira stanje, če potrebujemo več različnih stanj.
    """
    def clone(self):
        cloned = State()
        cloned.matrix = [col[:] for col in self.matrix]
        cloned.locked = [col[:] for col in self.locked]
        return cloned

    """
    Preveri, če je stanje veljavno.
    """
    def valid(self):
        columns = self.matrix
        rows = [list(row) for row in zip(*self.matrix)]
        blocks = [[self.matrix[x][y] for (x, y) in getBlockIndices(b)] for b in range(9)]

        for values in columns + rows + blocks:
            filled = [v for v in values if v is not None]
            unique = set(filled)
            if len(unique) != len(filled):
                return False

        return True

    """
    Preveri, če je stanje rešeno.
    """
    def solved(self):
        for col in self.matrix:
            for val in self.matrix[x]:
                if val is None:
                    return False
        return True

    """
    Opravi spremembo stanja, če je mogoča, in vrne novo stanje.
    """
    def mutate(self, x, y, value):
        new = self.clone()
        
        if self.locked[x][y]:
            raise Exception("Cannot edit a locked cell.")

        elif value not in range(1,10):
            raise Exception("Številka mora imeti vrednost med 1-9.")
        
        else:
            new.matrix[x][y] = value
        
        if not new.valid():
            raise Exception("Ni veljavna matrika")
        
        #optimatizacija
        return new
# test

s = State()
s.matrix = [
    [1, 2, 3,   4, 5, 6,   7, 8, 9],
    [4, 5, 6,   7, 8, 9,   1, 2, 3],
    [7, 8, 9,   1, 2, 3,   4, 5, 6],

    [2, 3, 4,   5, 6, 7,   8, 9, 1],
    [5, 6, 7,   8, 9, 1,   2, 3, 4],
    [8, 9, 1,   2, 3, 4,   5, 6, 7],

    [3, 4, 5,   6, 7, 8,   9, 1, 2],
    [6, 7, 8,   9, 1, 2,   3, 4, 5],
    [9, 1, 2,   3, 4, 5,   6, 7, 8]
]
print("Stanje 1 veljavno:", s.valid())

s.matrix[1][1] = 13
print("Stanje 2 veljavno:", s.valid())

s.matrix[1][1] = None
print("Stanje 3 veljavno:", s.valid())


print(s)

x = input("Naslednja poteza")
print(x)