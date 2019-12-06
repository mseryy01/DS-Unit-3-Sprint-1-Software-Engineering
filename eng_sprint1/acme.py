import random

class Product:
    """ Set up Product class"""
    def __init__(self, name, price=10, weight=20, flammability=0.5,
    identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Determine product's stealability"""
        steal = self.price / self.weight
        if steal < 0.5:
            return print("Not so stealable..")
        elif steal >= 0.5 and steal < 1.0:
            return print("Kinda stealable.")
        else:
            return print("Very stealable!")

    def explode(self):
        """Determines product's tendency to explode"""
        explode = self.flammability * self.weight
        if explode < 10:
            return print("...fizzle.")
        elif explode >= 10 and explode < 50:
            return print("...boom!")
        else:
            return print("...BABOOM!!")

class BoxingGlove(Product):
    """Subclass of Product with different parameters"""
    def __init__(self, weight=10):
        super().__init__(weight)

    def explode(self):
        """Overides explode function for BoxingGlove"""
        return print("...it's a glove.")

    def punch(self):
        """Determines punch strength"""
        if self.weight < 5:
            return print("That tickles.")
        elif self.weight >= 5 and self.weight < 15:
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
