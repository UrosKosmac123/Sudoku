
ŠTEVILO_DOVOLJENIH_NAPAK = 3

class Sudoku_Napake:

    pass


class Sudoku_Tabela:

    def __init__(self, datoteka_tabele):
        self.tabela = self.__vstvari_tabelo(datoteka_tabele)

    def __vstvari_tabelo(self, datoteka_tabele):
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

    def zacetek(self):
        self.konec_igre = False
        self.uganka = []
        for i in range(9):
            self.uganka.append([])
            for j in range(9):
                self.uganka[i].append(self.start_puzzle[i][j])

    def preveri_zmago(self):
        for vrstica in range(9):
            if not __self.preveri_vrstico(vrstica):
                return False
        for stolpec in  range(9):
            if not __self.preveri_stolpec(stolpec):
                return False
        for vrstica in range(3):
            for stolpec in range(3):
                if not __self.preveri_3x3_blok(vrstica, stolpec):
                    return False
        
        self.konec_igre = True
        return True

    def __preveri_blok_stevil(self, blok):
        return set(blok) == set(range(1,10))

    def __preveri_vrstico(self, vrstica):
        return __preveri_blok_stevil(self.uganka[vrstica])

    def __preveri_stolpec(self, stolpec):
        return __preveri_blok_stevil(
            [self.uganka[vrstica][stolpec] for vrstica in range(9)])

    def __preveri_3x3_blok(self, vrstica, stolpec):
        return __preveri_blok_stevil(
            [
                self.uganka[i][j]
                for i in range((3*vrstica, 3*(vrstica+1))
                for j in range(3*stolpec, 3*(stolpec+1))
            ]
        )