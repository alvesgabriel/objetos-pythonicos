=========================
Tests with class `Dog`
=========================

A `Dog` instance has a debug representation (`repr`) that
permite to build a equal instance::

    >>> from dog import Dog
    >>> rex = Dog('Rex')
    >>> rex
    Dog('Rex')
    >>> rex2 = eval(repr(rex))
    >>> rex2.name
    'Rex'
    >>> rex2
    Dog('Rex')
    >>> rex == rex2
    True

The friendly representation is only the dog name::

    >>> print(rex)
    Rex

Some attributes, like `qt_paws` are defined in `Dog` class and inherited
by instances::

    >>> rex.qt_paws
    4

The method `bark` has a optional number of barks, if the dog is angry,
it always barks double::

    >>> rex.bark()
    Rex: Au!
    >>> rex.bark(2)
    Rex: Au! Au!
    >>> rex.angry = True
    >>> rex.bark(3)
    Rex: Au! Au! Au! Au! Au! Au!
