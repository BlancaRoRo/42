# Clase Planta: age, grow, getters y setters

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")

    def grow(self, cm: float) -> None:
        self.set_height(round(self._height + cm, 1))

    def age(self, days: int) -> None:
        self.set_age(days + self._days)

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


# Clase Flower:bloom, getcolor
class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
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


# Tree:produce_shade
class Tree(Plant):
    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


# Vegetable:overwrite grow y age -> nutritional_value
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

    def grow(self, cm: float) -> None:
        super().grow(cm)
        self._nutritional_value += cm * 0.2

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days * 0.58


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    vegetable.age(20)
    vegetable.grow(42)
    vegetable.show()
