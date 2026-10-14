# Plant: clase anidada _Stats: conteo de llamadas a métodos
# staticmethod: more_than_year
# classmethod: constructor con otros valores por defecto
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self._stats = Plant._Stats()

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._show_calls = 0
            self._age_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def grow(self, cm: float) -> None:
        self._stats.add_grow()
        self.set_height(round(self._height + cm, 1))

    def age(self, days: int) -> None:
        self._stats.add_age()
        self.set_age(days + self._days)

    @staticmethod
    def more_than_year(days: int) -> bool:
        if days <= 365:
            return False
        return True

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print("Error, height can't be negative")
            return False
        else:
            self._height = height
            return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print("Error, age can't be negative")
            return False
        else:
            self._days = days
            return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._days

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant._Stats":
        return self._stats


# Flower:bloom booleano que se resuelve en el show
class Flower(Plant):

    def __init__(
            self, name: str, height: float, days: int, color: str
            ) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._blooming = False

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


# Tree: clase anidada TreeStats para conteo de _shade_calls
class Tree(Plant):
    def __init__(
            self, name: str, height: float, days: int, trunk_diameter: float
            ) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(
            f"Tree {self._name} now produces a shade of {self._height:.1f}cm "
            f"long and {self._trunk_diameter:.1f}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


# Vegetable:
class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nutritional_value)}")

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days * 0.58

    def grow(self, cm: float) -> None:
        super().grow(cm)
        self._nutritional_value += cm * 0.2


# Seed:bloom (booleano), semillas desprendidas por defecto 42
# number_seeds es como un get de seeds
class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def number_seeds(self) -> int:
        return self._seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


# Método aislado que acepta objetos tipo planta
def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.more_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.more_than_year(400)}")
    print()
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    display_stats(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    display_stats(flower)
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_stats(tree)
    print()
    print("=== Seed")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow(30)
    seed.age(20)
    seed.bloom()
    seed.show()
    display_stats(seed)
    print()
    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_stats(anonymous)
