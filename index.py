#ANCHOR Land animal imports
from animals import Capybara
from animals import Echidna 
from animals import Fox
from animals import Hedgehog
from animals import Pangolin

#ANCHOR Slither animal imports
from animals import Anaconda
from animals import Cobra
from animals import Mamba
from animals import Python
from animals import Taipan

#ANCHOR Swim animal imports
from animals import Axolotl
from animals import Eel
from animals import Goldfish
from animals import Koi
from animals import Tuna

#ANCHOR Attraction imports
from attractions import Petting_Zoo
from attractions import Snake_Pit
from attractions import Wetlands

#ANCHOR Create land animals 
pango = Pangolin("Pango", "pangolin", "evening", "ants")
sonic = Hedgehog("Sonic", "hedgehog", "morning", "golden rings", 9876)
yusuke = Fox("Yusuke", "fox", "afternoon", "Mystery Food X")
knuckles = Echidna("Knuckles", "echidna", "morning", "golden rings")
captain_america = Capybara("Captain America", "capybara", "evening", "freedom")

#ANCHOR Create swim animals
axl_rose = Axolotl("Axl Rose", "axolotl", "a microphone")
kai = Koi("Kai", "koi fish", "leftover chinese")
sparky = Eel("Sparky", "eel", "literal electricity")
brains = Goldfish("Brains", "goldfish", "fish food")
riley = Tuna("Riley", "tuna", "probably pizza")

#ANCHOR Create slither animals
jetbrain = Python("JetBrain", "python", "error messages")
takamaki = Anaconda("Takamaki", "anaconda", "cake")
number_five = Mamba("Number Five", "mamba", "gin and juice")
kai_but_funnier = Cobra("Kai but Funnier", "cobra", "karate gi")
numba_one = Taipan("Numba One", "taipan", "communism")

#ANCHOR Create attractions
pet_planet = Petting_Zoo("Pet Planet", "Home the finest land animals Tennessee has ever seen, Pet planet offers to satiate your wildest petting zoo dreams.")

hissteria = Snake_Pit("Hissteria", "All bite and no bark, these slithering sons of guns are precariously placed for your viewing pleasure. (anti-venom not included with admissions ticket)")

lazy_river = Wetlands("Lazy River", "This attraction might be lazy, but these wet'n'wild animals are anything but. When you come on down, don't forget to stop by our gift shop and pick up one of our Crazy Critter Collective™ brand ponchos to remember us by!")

#ANCHOR Add animals to attractions
pet_planet.animals.append(pango)
pet_planet.animals.append(sonic)
pet_planet.animals.append(yusuke)
pet_planet.animals.append(knuckles)
pet_planet.animals.append(captain_america)

hissteria.animals.append(jetbrain)
hissteria.animals.append(takamaki)
hissteria.animals.append(kai_but_funnier)
hissteria.animals.append(numba_one)
hissteria.animals.append(number_five)

lazy_river.animals.append(axl_rose)
lazy_river.animals.append(sparky)
lazy_river.animals.append(brains)
lazy_river.animals.append(riley)
lazy_river.animals.append(kai)

print(pet_planet.last_animal_added)