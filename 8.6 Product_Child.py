class Product:

    MIN_PRIJS = 0.99

    def __init__(self, nw_prijs=0.99, aantal_in_voorraad=0):
        if nw_prijs < Product.MIN_PRIJS:
           raise ValueError(f"de opgegeven pijs is {nw_prijs}, maar mag niet lager zijn dan {Product.MIN_PRIJS}")
        self._prijs = nw_prijs
        self.aantal_in_voorraad = aantal_in_voorraad

    @property
    def prijs(self):
        return self._prijs

    @prijs.setter
    def prijs(self, nw_prijs):
        if nw_prijs < Product.MIN_PRIJS:
            raise ValueError(f"de opgegeven pijs is {nw_prijs}, maar mag niet lager zijn dan {Product.MIN_PRIJS}")
        self._prijs = nw_prijs

    def bestellen(self, aantal):
        if aantal > self.aantal_in_voorraad:
            print(f"Onvoldoende voorraad")
            print(f"De voorraad bedraagt {self.aantal_in_voorraad}")
        else:
            print(f"Bestelling van {aantal} uitgevoerd.")
            self.aantal_in_voorraad -= aantal

    def geef_korting(self, korting):
        self._prijs = self._prijs * (1 - ( korting / 100 ))



class Boek(Product):
    def __init__(self, titel, auteur, uitgever):
        Product.__init__(self, nw_prijs=0.99, aantal_in_voorraad=0)
        self.titel = titel
        self.auteur = auteur
        self.uitgever = uitgever

class DVD(Product):
    def __init__(self, titel, auteur, uitgever):
        Product.__init__(self, nw_prijs=0.99, aantal_in_voorraad=0)
        self.titel = titel
        self.auteur = auteur
        self.uitgever = uitgever

    def geef_korting(self, korting):
        print(f"Geen korting op DVD's\n")



boek1 = Boek("De Mol", "Saskia Martens", "Lannoo")
boek1.prijs = 20
boek1.geef_korting(3)
boek1.aantal_in_voorraad = 100

print(f"{boek1.titel} van {boek1.auteur}; uitgeverij {boek1.uitgever}")
print(f"prijs : {boek1.prijs} Euro")
print(f"Aantal in voorraad : {boek1.aantal_in_voorraad}\n")

boek1.bestellen(10)
print(f"Aantal in voorraad : {boek1.aantal_in_voorraad}\n")

DVD1 = DVD("Bohemian Rhapsody", "Queen", "EMI")
DVD1.prijs = 20
DVD1.geef_korting(10)


print(f"{DVD1.titel} van {DVD1.auteur}; uitgeverij {DVD1.uitgever}")
print(f"prijs : {DVD1.prijs} Euro")
print(f"Aantal in voorraad : {DVD1.aantal_in_voorraad}\n")