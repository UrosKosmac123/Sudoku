IGRE = ["Easy", "Normal", "Difficult"]
VELIKOST_KVADRATKA = 50
SIRINA = DOLZINA = VELIKOST_KVADRATKA * 9


class Sudoku_Napake:

    pass


class Sudoku_Tabela:

    def __init__(self, datoteka_tabele):
        self.tabela = __vstvari_tabelo(datoteka_tabele)

    def vstvari_tabelo(self, datoteka_tabele):
        #Sudoku tabela kot matrika
        tabela = []

        for vrstica in datoteka_tabele:
            vrstica = vrstica.strip()
        #če je dolžina vrstice različna od 9 kličemo Sudoku_Napake
        if len(vrstica) != 9:
           raise Sudoku_Napake("Vsaka vrstice v Sudoku tabeli je dolžine devetih znakov")

        #seznam za vrstico   
        tabela.append([])

        #naredimo zanko čez vsak znak vrstice
        for stevilo in vrstica:
            if not stevilo.is_integer() and stevilo not in range(1,10):
                raise Sudoku_Napake("Dovoljena so samo cela števila med 1-9")
            tabela[-1].append(int(stevilo))

        if len(tabela) != 9:
            raise Sudoku_Napake("Vsaka tabela mora imeti 9 vrstic")

        return tabela

class SudokuIgra: 
    #Sudoku igra, hrani vsa stanja igre
    #in preverja, če je igra končana.

    def __init__(self, datoteka_tabele):
        self.datoteka_tabele = datoteka_tabele
        self.zacni_igro = Sudoku_Tabela(datoteka_tabele).tabela

    #def start(self):
        #self.konec_igre = False
        #self.uganka = []i
        #for i in range(9):
