from ex3 import Creature, TransformCapability, TransformCreatureFactory


def test_capability(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    print(" base:")
    test_capability(factory.create_base())
    print(" evolved:")
    test_capability(factory.create_evolved())
