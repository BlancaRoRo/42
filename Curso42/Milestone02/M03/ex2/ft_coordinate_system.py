import math
# tupla: tuple[tipo de dato, ...(varios datos de ese tipo)] = ()
# es innmutable, no se puede cambiar el valor de sus elementos


# Funcnionalidad: Pide ingresar coordenadas en un formato específico
# y de 3 valores
# Devuelve una tupla de esas coordenadas como float
def get_player_pos() -> tuple[float, ...]:
    while True:
        coordenates = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        # si no hay exactamente 3 valores, el desempaquetado lanza ValueError
        try:
            try:
                x, y, z = coordenates.split(",")
            except ValueError:
                raise ValueError("Invalid syntax")

            first_tuple: tuple[float, ...] = ()
            valid: bool = True
            try:
                for i in (x, y, z):
                    first_tuple = first_tuple + (float(i),)
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                valid = False
            if valid:
                return first_tuple
        except ValueError as e:
            print(f"{e}")


# Funcionalidad: Calcula la distancia euclidiana entre dos puntos
# con 3 coordenadas
def euclidean_distance(x: float, y: float, z: float,
                       x2: float, y2: float, z2: float) -> float:
    return (math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos: tuple[float, ...] = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    x, y, z = first_pos
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance_center = euclidean_distance(x, y, z, 0, 0, 0)
    print(f"Distance to center: {round(distance_center, 4)}\n")
    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    distance_two_points = euclidean_distance(x, y, z, x2, y2, z2)
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance_two_points, 4)}")
