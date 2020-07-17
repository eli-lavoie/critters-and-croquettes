class Petting_Zoo:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        print(f"When you come by {self.attraction_name}, be sure to say hi to our friends:")
        for animal in self.animals:
            print(f"•{animal.name} the {animal.species}")
    
    def __str__(self):
        return self.description

    @property
    def last_animal_added(self):
        return self.animals[-1]