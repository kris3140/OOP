class Klant:
    def __init__(self):
        self.lijst = []

class Klanten(Klant):
    def __iter__(self):
        self.index = -1
        self.aantal = len(self.lijst)
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.aantal:
            raise StopIteration
        return self.lijst[self.index]

    def add_klant(self, name):
        self.lijst.append(name)
        return self.lijst


mijnklanten = Klanten()
mijnklanten.add_klant("Peeters")
mijnklanten.add_klant("Janssens")
mijnklanten.add_klant("Willems")

myiter = iter(mijnklanten)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()

for klant in mijnklanten:
    print(klant)








