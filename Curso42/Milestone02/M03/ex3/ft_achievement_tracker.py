import random
# set  = {}. NO pueden ser repetidos, no orden de entrada (sí ordenado)y
# funciona mediante hashing, por eso es tan rápido. Código para
# comparar un elemento por su valor
# lista de logros
achievements = ["Crafting Genius", "Strategist",
                "World Savior", "Speed Runner",
                "Survivor", "Master Explorer",
                "Treasure Hunter", "Unstoppable",
                "First Steps", "Collector Supreme",
                "Untouchable", "Sharp Mind",
                "Boss Slayer", "Hidden Path Finder"]


# Funcionalidad: Genera un conjunto aleatorio de logros entre 3-10
# Devuelve un set de logros aleatorios
def gen_player_achievements() -> set[str]:
    rng = random.randint(3, 10)
    return set(random.sample(achievements, rng))


# Funcionlidad: Genera un conjunto de logros para cada jugador
# Muestra los distintos logros de cada jugador, los comunes,
# los únicos y los que le faltan
if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    first_set: set[str] = gen_player_achievements()
    print(f"Player Alice: {first_set}")
    second_set: set[str] = gen_player_achievements()
    print(f"Player Bob: {second_set}")
    third_set: set[str] = gen_player_achievements()
    print(f"Player Charlie: {third_set}")
    fourth_set: set[str] = gen_player_achievements()
    print(f"Player Dylan: {fourth_set}\n")
    print("All distinct achievements: "
          f"{set.union(first_set, second_set, third_set, fourth_set)}\n")
    print("Common achievements: "
          f"{set.intersection(first_set, second_set, third_set, fourth_set)}"
          "\n")
    print("Only Alice has: "
          f"{first_set.difference(second_set, third_set, fourth_set)}")
    print("Only Bob has: "
          f"{second_set.difference(first_set, third_set, fourth_set)}")
    print("Only Charlie has: "
          f"{third_set.difference(second_set, first_set, fourth_set)}")
    print("Only Dylan has: "
          f"{fourth_set.difference(second_set, third_set, first_set)}\n")
    achievements_set: set[str] = set(achievements)
    print(f"Alice is missing: {achievements_set.difference(first_set)}")
    print(f"Bob is missing: {achievements_set.difference(second_set)}")
    print(f"Charlie is missing: {achievements_set.difference(third_set)}")
    print(f"Dylan is missing: {achievements_set.difference(fourth_set)}")
