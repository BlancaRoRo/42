from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_entity: str) -> None:
        self._name = name
        self._type_entity = type_entity

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type_entity} type Creature"


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._state = False
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
