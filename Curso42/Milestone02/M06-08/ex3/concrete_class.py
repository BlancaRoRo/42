from .abstract_class import Creature, CreatureFactory, TransformCapability


class Flameling(Creature):
    # if I don't assign the name and type variables in this
    # constructor, the parent class does it
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"
    # describe is not needed, since it is already implemented
    # by the parent class


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


# Creature and TransformCapability classes
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        # to get the class state, I have to inherit the constructor
        # methods are inherited, not the constructor's attributes.
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._state:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self._state = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._state = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._state:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self._state = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._state = False
        return "Morphagon stabilizes its form."


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
