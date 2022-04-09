class Klant:
    # hier maken we de collection aan
    # er is een lijst waar we via de index van de naam kunnen iteraten
    # er is een dictionary waar naam en saldo in staan
    # dus de naam staat zowel in de lijst (als iterator) als in de dict (link met saldo)
    def __init__(self):
        self.keys_list = []
        self.dict = {}

class Klanten(Klant):
    def __iter__(self):
        # we beginnen bij index -1 zodat de iterator begint met index
        # we tellen ook het aantal elementen zodat we de iterator kunnen stoppen
        self.index = -1
        self.aantal_keys = len(self.keys_list)
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.aantal_keys:
            raise StopIteration
        # key = de naam uit de lijst en dict[key] is het saldo van die naam
        key = self.keys_list[self.index]
        klant = f"{key}  {self.dict[key]}"
        return klant

    def add_klant(self, naam, saldo=0):
        self.keys_list.append(naam)
        self.dict.update({naam : saldo})
        return self.dict


mijnklanten = Klanten()
mijnklanten.add_klant("Peeters")
mijnklanten.add_klant("Janssens")
mijnklanten.add_klant("Willems")

# myiter = iter(mijnklanten)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print()

for klant in mijnklanten:
    print(klant)
