import random

player_name = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
# comprehensions: item for item in iterable if condicion
if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {player_name}")
    # lista con nombres capitalizados (se capitalizan)
    list_capitalized = [name.capitalize() for name in player_name]
    print(f"New list with all names capitalized: {list_capitalized}")
    # lista con nombres ya capitalizados (se filtran)
    only_capitalized = [name for name in player_name
                        if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}\n")
    # diccionario con nombres capitalizados y puntuaciones aleatorias
    dictionary_capitalized: dict[str, int] = {
        name: random.randint(100, 1000) for name in list_capitalized}
    print(f"Score dict: {dictionary_capitalized}")
    average = round(sum(dictionary_capitalized.values())
                    / len(dictionary_capitalized.keys()), 2)
    print(f"Score average is {average}")
    higher_score: dict[str, int] = {
        item: dictionary_capitalized[item]
        for item in dictionary_capitalized
        if dictionary_capitalized[item] > average}
    print(f"High scores: {higher_score}")
