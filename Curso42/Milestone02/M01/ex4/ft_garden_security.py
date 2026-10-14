# privatización de atributos, getters y setters.
# Se pone primero el valor 0 por defecto en el constructor por si hay
# errores en el setter
# tener un valor ya puesto.
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
        self.set_age(self._days + days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        else:
            self._height = height
            return True

    def set_age(self, days: int) -> bool:
        if days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        else:
            self._days = days
            return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    plant.show()
    tests = [(25, 30), (-5, -3)]

    for height, days in tests:
        if plant.set_height(height):
            print(f"Height updated: {height}cm")
        else:
            print("Height update rejected")
        if plant.set_age(days):
            print(f"Age updated: {days} days")
        else:
            print("Age update rejected")
    print()
    print("Current state: ", end="")
    plant.show()
