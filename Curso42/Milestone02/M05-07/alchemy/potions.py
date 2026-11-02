# elements de la raíz
# si pongo solo import elements no sabe como se llaman los métodos
from elements import create_fire, create_water
# elements de alchemy
from .elements import create_earth, create_air


def healing_potion() -> str:
    return (f"Healing potion brewed with '{create_earth()}'"
            f" and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with"
            f" '{create_fire()}' and '{create_water()}'")
