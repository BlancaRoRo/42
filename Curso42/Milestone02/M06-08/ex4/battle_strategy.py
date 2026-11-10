from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    @abstractmethod
    def act() -> None:
    
    def is_valid(Creature) -> bool:
        if isinstance()

class NormalStrategy(BattleStrategy):

    def attack(self) -> str:

class AggressiveStrategy(BattleStrategy):
    
