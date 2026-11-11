from ex4 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, ErrorInstance
)
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def battle(
        list_opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    len_list = len(list_opponents)
    print("*** Tournament ***")
    print(f"{len_list} opponents involved")
    try:
        for i in range(0, len_list):
            factory1, strategy1 = list_opponents[i]
            for j in range(i + 1, len_list):
                factory2, strategy2 = list_opponents[j]
                creature1 = factory1.create_base()
                creature2 = factory2.create_base()
                print("\n* Battle *")
                print(creature1.describe())
                print(" vs.")
                print(creature2.describe())
                print(" now fight!")
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
    except ErrorInstance as e:
        print(e)


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    list_opponents: list[tuple[CreatureFactory, BattleStrategy]] = []
    list_opponents.append((FlameFactory(), NormalStrategy()))
    list_opponents.append((TransformCreatureFactory(), AggressiveStrategy()))
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle(list_opponents)
    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]\n")
    list_opponents.pop()
    list_opponents.pop()
    list_opponents.append((TransformCreatureFactory(), AggressiveStrategy()))
    list_opponents.append((FlameFactory(), AggressiveStrategy()))
    battle(list_opponents)
