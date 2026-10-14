class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    planta1 = Plant("Rose", 25, 30)
    Plant.show(planta1)
    planta2 = Plant("Sunflower", 80, 45)
    Plant.show(planta2)
    planta3 = Plant("Cactus", 15, 120)
    Plant.show(planta3)


if __name__ == "__main__":
    ft_garden_data()
