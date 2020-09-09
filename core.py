
def getBlockIndices(block):
    x = (block % 3) * 3
    y = (block // 3) * 3
    return [[x + i % 3, y + i // 3] for i in range(9)]

COLOR_YELLOW = u"\u001b[34m"

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
        s = ""
        s += u"\u001b[34m    1   2   3   4   5   6   7   8   9\u001b[0m\n"
        rows = [list(row) for row in zip(*self.matrix)]
        for y, row in enumerate(rows):
            s += u"\u001b[34m" + str(y + 1) + u" \u001b[0m"
            for x, val in enumerate(row):
                v = str(val)
                if val is None:
                    v = "-"
                if self.locked[x][y]:
                    s += " [" + u"\u001b[33m"+ v + u"\u001b[0m" + "]"
                else:
                    s += "  " + v + " "
            s += "\n"

        return s

    """
    Klonira stanje, če potrebujemo več različnih stanj.
    """
    def clone(self):
        cloned = State()
        cloned.matrix = [col[:] for col in self.matrix]
        cloned.locked = [col[:] for col in self.locked]
        return cloned

    def generate(self):
        base  = 3
        side  = base*base

        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        from random import sample
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            board[p//side][p%side] = None 

        self.matrix = board
        self.locked = [[val is not None for val in col] for col in self.matrix]

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
            for val in col:
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
            raise Exception("Napačna vrednost")
        
        #optimatizacija
        return new



