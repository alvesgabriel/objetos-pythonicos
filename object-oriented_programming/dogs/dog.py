class Mammal:
    """
    a warm-blooded vertebrate animal of a class that is distinguished by the
    possession of hair or fur, the secretion of milk by females for the
    nourishment of the young, and (typically) the birth of live young.
    """


class Dog(Mammal):
    qt_paws = 4
    carnivorous = True
    angry = False

    def __init__(self, name):
        self.name = name

    def bark(self, qty=1):
        qty += self.angry * qty
        print(f"{self.name}:{' Au!' * qty}")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Dog('{self.name}')"

    def __eq__(self, other):
        return isinstance(other, Dog) and self.__dict__ == other.__dict__
