from random import sample

class State:
    """Stanje sudoku aplikacije."""

    def __init__(self, generate: bool = False):
        """
        Konstruktor stanja, ki inicializira novo prazno matriko.
        Opcijsko generira novo matriko.
        """
        self.matrix = [[None for y in range(9)] for x in range(9)]
        self.locked = [[False for y in range(9)] for x in range(9)]

        if (generate):
            self.generate()

    def __str__(self) -> str:
        """Izpis stanja v preprosti berljivi obliki."""
        return "\n".join(
            [
                " ".join([str(v) if v is not None else "-" for v in col])
                for col in self.matrix
            ]
        )

    def clone(self):
        """Klonira stanje, če potrebujemo več različnih stanj."""
        cloned = State()
        cloned.matrix = [col[:] for col in self.matrix]
        cloned.locked = [col[:] for col in self.locked]
        return cloned

    def generate(self):
        """Generira novo začetno stanje."""
        def pattern(r, c): return (3*(r % 3)+r//3+c) % 9
        def shuffle(s): return sample(s, len(s))

        base = range(3)
        rows = [g*3 + r for g in shuffle(base) for r in shuffle(base)]
        cols = [g*3 + c for g in shuffle(base) for c in shuffle(base)]
        nums = shuffle(range(1, 10))

        self.matrix = [[nums[pattern(r, c)] for c in cols] for r in rows]
        self.locked = [[True for y in range(9)] for x in range(9)]

        for p in sample(range(81), 81 * 3//4):
            self.matrix[p//9][p % 9] = None
            self.locked[p//9][p % 9] = False

        return self

    def valid(self) -> bool:
        """Preveri, če je stanje veljavno."""
        def getBlockIndices(block: int):
            x = (block % 3) * 3
            y = (block // 3) * 3
            return [[x + i % 3, y + i // 3] for i in range(9)]

        columns = self.matrix
        rows = [list(row) for row in zip(*self.matrix)]
        blocks = [[self.matrix[x][y]
                   for (x, y) in getBlockIndices(b)] for b in range(9)]

        for values in columns + rows + blocks:
            filled = [v for v in values if v is not None]
            unique = set(filled)
            if len(unique) != len(filled):
                return False

        return True

    def solved(self) -> bool:
        """Preveri, če je stanje rešeno."""

        for row in self.matrix:
            for val in row:
                if val is None:
                    return False
        return True

    def progress(self) -> int:
        """ Vrne število izpolnjenih celic."""
        return sum([1 if value else 0 for row in self.matrix for value in row])

    def mutate(self, x: int, y: int, value: int):
        """Opravi spremembo stanja, če je mogoča, in vrne novo stanje."""

        new = self.clone()

        if x not in range(0, 9) or y not in range(0, 9):
            raise Exception("({},{}) are not valid coordinates.".format(x, y))

        if value not in range(1, 10):
            raise Exception(str(value) + " is not a valid value.")

        if self.locked[x][y]:
            raise Exception("Cannot edit a locked cell.")

        if value in self.matrix[x]:
            raise Exception(
                "Value {} is already present in row {}".format(value, x+1))

        if value in [row[y] for row in self.matrix]:
            raise Exception(
                "Value {} is already present in column {}.".format(value, y+1))

        if value in [value for row in self.matrix[(x//3)*3:(x//3)*3+3] for value in row[(y//3)*3:(y//3)*3+3]]:
            raise Exception("Value {} is already present in block.".format(value))

        new.matrix[x][y] = value

        return new

