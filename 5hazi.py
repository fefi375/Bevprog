class Ceg:
    def __init__(self, nev, rang, beev, fizetes)->None:
        self.nev=nev
        self.rang=rang
        self.beev=beev
        self.fizetes=fizetes
        self.beev=0

    def femeles(self, emeles=10000):
        self.fizetes+=emeles
        print("A fejleszto fizetese: {0}".format(self.fizetes))
    def ev(self):
        self.beev+=1
    
    def rangja(self):
        if self.beev<1:
            self.rang="Intern"
        elif self.beev<2 and self.beev >1:
            self.rang="Junior"
        elif self.beev>2 and self.beev<5:
            self.rang="Medior"
        elif self.beev>5:
            self.rang="Senior"
            
        print("A fejlesztő rangja: "+self.rang)


def main():
    a1=Ceg("Jóska", "Junior", 0, 0)
    a1.femeles()
    a1.ev()
    a1.rangja()
    
    
    
    
    
if __name__=="__main__":
    main()