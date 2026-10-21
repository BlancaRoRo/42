import random
import typing
# listas de jugadores y acciones
name_player: list[str] = ["bob", "alice", "dylan", "charlie"]
actions: list[str] = ["run", "eat", "sleep", "move",
                      "climb", "swim", "grab", "release"]


# generador de jugador y eventos
# devuelve una tupla con el nombre del jugador y la acción
def gen_event() -> typing.Generator[tuple[str, ...], None, None]:
    tuple_gen: tuple[str, ...] = ()
    while True:
        tuple_gen = (random.choice(name_player), random.choice(actions))
        yield tuple_gen


# generador de jugador y eventos a partir de una lista de tuplas
# devuelve el nombre del jugador y la acción eliminada de la lista
# se usa choice ya que al eliminar elementos de la lista no se pueden repetir
def consume_event(
        gen_list: list[tuple[str, ...]]
) -> typing.Generator[tuple[str, ...], None, None]:
    while gen_list:
        name: tuple[str, ...] = ()
        name = random.choice(gen_list)
        gen_list.remove(name)
        yield name


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    tuple_list: list[tuple[str, ...]] = []
    tuple_gen: tuple[str, ...] = ()
    generator = gen_event()
    for i in range(0, 1000):
        tuple_gen = (next(generator))
        print(f"Event {i}: Player {tuple_gen[0]} did action {tuple_gen[1]}")
    for i in range(0, 10):
        tuple_list.append(next(generator))
    print(f"Built list of 10 events: {tuple_list}")
    for evento in consume_event(tuple_list):
        print(f"Got event from list: {evento}")
        print(f"Remains in list: {tuple_list}")
