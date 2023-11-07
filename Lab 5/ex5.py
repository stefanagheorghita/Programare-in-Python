class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def reproduction(self):
        pass


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color, diet):
        super().__init__(name)
        self.fur_color = fur_color
        self.diet = diet
        self.habitat = habitat

    def move(self):
        print(str(self.name) + " can walk.")

    def reproduction(self):
        print(str(self.name) + " give birth to their young.")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def move(self):
        print(str(self.name) + " can fly.")

    def reproduction(self):
        print(str(self.name) + "  lay eggs.")


class Fish(Animal):
    def __init__(self, name, place_to_live, dimensions):
        super().__init__(name)
        self.dimensions = dimensions
        self.place_to_live = place_to_live

    def move(self):
        print(str(self.name) + " can swim.")

    def reproduction(self):
        print("Fish lay eggs.")

    def breathe_underwater(self):
        print(str(self.name) + " can breathe underwater.")

    def verify_dimension(self):
        if self.dimensions < 10:
            print("Small fish")
        elif self.dimensions < 20:
            print("Medium fish")
        else:
            print("Large fish")


mammal = Mammal("Dog", "House", "Brown", "Omnivore")
mammal.move()
mammal.reproduction()

bird = Bird("Eagle", "Large")
bird.move()
bird.reproduction()

fish = Fish("Clown fish", "Ocean", 15)
fish.move()
fish.reproduction()
fish.breathe_underwater()
fish.verify_dimension()
