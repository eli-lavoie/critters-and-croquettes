from datetime import date

#Land Animals
class Pangolin:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

class Hedgehog:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

class Echidna:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

class Fox:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

class Capybara:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

#Swim Animals
class Axolotl:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Eel:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Tuna:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

#Slither Animals
class Python:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.sliterhing = True

class Anaconda:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.sliterhing = True

class Mamba:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.sliterhing = True

class Cobra:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.sliterhing = True

class Taipan:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.sliterhing = True

#Creation Time
pango = Pangolin("Pango", "pangolin", "evening")
sonic = Hedgehog("Sonic", "hedgehog", "morning")
yusuke = Fox("Yusuke", "fox", "afternoon")
knuckles = Echidna("Knuckles", "echidna", "morning")
captain_america = Capybara("Captain America", "capybara", "evening")

axl_rose = Axolotl("Axl Rose", "axolotl")
kai = Koi("Kai", "koi fish")
sparky = Eel("Sparky", "eel")
brains = Goldfish("Brains", "goldfish")
riley = Tuna("Riley", "tuna")

jetbrain = Python("JetBrain", "python")
takamaki = Anaconda("Takamaki", "anaconda")
number_five = Mamba("Number Five", "mamba")
kai_but_funnier = Cobra("Kai but Funnier", "cobra")
numba_one = Taipan("Numba One", "taipan")

