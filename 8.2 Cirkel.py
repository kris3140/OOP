from math import pi

class GeometrischeFiguren():

    __slots__ = ()


class Cirkel(GeometrischeFiguren):

    '''Deze klasse laat toe bewerkingen op een cirkel uit te voeren'''

    __slots__ = ('_straal', 'omtrek', 'oppervlakte')

    def __init__(self, new_straal):
        if new_straal <= 0:
            raise ValueError('Straal moet groter zijn dan 0')
        self._straal = new_straal
        self.bereken_oppervlakte()
        self.bereken_omtrek()

    @property
    def straal(self):
        return self._straal

    @straal.setter
    def straal(self, new_straal):
        if new_straal <= 0:
            raise ValueError('Straal moet groter zijn dan nul')

    def bereken_oppervlakte(self):
            self.oppervlakte = pi * self._straal ** 2

    def bereken_omtrek(self):
            self.omtrek =  pi * self._straal * 2

    def __str__(self):
        info = (f"straal: {self.straal:.2f} \n"
                f"omtrek : {self.omtrek:.2f} \n"
                f"oppervlakte: {self.oppervlakte:.2f}")
        return info

    def __repr__(self):
        return f"Cirkel({self._straal})"




# object aanmaken
c1 = Cirkel(3)

print('__str__ :')
print(c1)
print()
print('__repr__ :')
print(repr(c1))
print()

print('Docstring :')
print(Cirkel.__doc__)
print()

print('dir: ')
print(dir(Cirkel))
print()
#
# print('dict: ')
# print(c1.__dict__)

c1.straal = 1
#
# c1.zijde = 5
# print(c1.zijde)


