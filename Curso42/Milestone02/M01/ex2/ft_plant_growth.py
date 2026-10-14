class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self, cm: float) -> None:
        self.height = round(self.height + cm, 1)

    def age(self, days: int) -> None:
        self.days += days


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    days = 7
    my_plant = Plant("Rose", 25, 30)
    start_height = my_plant.height
    my_plant.show()
    for i in range(1, days + 1):
        print(f"=== Day {i} ===")
        my_plant.grow(0.8)
        my_plant.age(1)
        my_plant.show()
    print(f"Growth this week: {round(my_plant.height - start_height, 1)}cm")
