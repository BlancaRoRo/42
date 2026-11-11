from abc import ABC, abstractmethod
from ex3 import TransformCapability, Creature


class ErrorInstance(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ErrorInstance(
                "Battle error, aborting tournament: Invalid Creature "
                f"'{type(creature).__name__}' for this normal strategy")
        else:
            return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise ErrorInstance(
                "Battle error, aborting tournament: Invalid Creature "
                f"'{type(creature).__name__}' for this aggressive strategy")
        else:
            return "\n".join([creature.transform(),
                              creature.attack(),
                              creature.revert()])

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False
