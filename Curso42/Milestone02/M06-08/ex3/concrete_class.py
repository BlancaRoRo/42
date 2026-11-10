from .abstract_class import Creature, CreatureFactory, TransformCapability


class Flameling(Creature):
    # si no asigno las variables name y type a este
    # constructor, lo hace la clase padre
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"
    # describe no es necesario, pues ya lo implementa
    # la clase padre


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


# Creature y TransformCapability clases
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        # para que me pille el state de clase, tengo que heredar el constructor
        # se heredan los métodos no los atributos del constructor.
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
        super().__init__("Morphagon", "Normal/Dragon")
        Creature.__init__(self, "Shiftling", "Normal")
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
