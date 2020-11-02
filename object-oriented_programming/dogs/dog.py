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


class BigMixin:
    """
    Mixin: change bark
    """
    def bark(self, qty=1):
        qty += self.angry * qty
        print(f"{self.name}:{' Wuff!' * qty}")


class Mastiff(BigMixin, Dog):
    """
    Mastiff barks diferent

    >>> atos = Mastiff('Atos')
    >>> atos.bark()
    Atos: Wuff!
    """


class StBernard(BigMixin, Dog):
    """
    St. Bernard serve brandy

    >>> sansao = StBernard('Sansao')
    >>> sansao.bark()
    Sansao: Wuff!
    >>> sansao.serve()
    Sansao serves brandy (9 doses left)
    >>> sansao.doses = 1
    >>> sansao.serve()
    Sansao serves brandy (0 doses left)
    >>> sansao.serve()
    Traceback (most recent call last):
      ...
    ValueError: Brandy ends!
    """
    def __init__(self, name):
        super().__init__(name)
        self.doses = 10

    def serve(self):
        if self.doses == 0:
            raise ValueError("Brandy ends!")
        self.doses -= 1
        msg = f"{self.name} serves brandy ({self.doses} doses left)"
        print(msg)
