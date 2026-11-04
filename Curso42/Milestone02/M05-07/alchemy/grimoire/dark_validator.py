# import ingenuo al principio del fichero: cuando se ejecuta, dark_spellbook
# está a medias y dark_spell_allowed_ingredients todavía no existe
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_valid = dark_spell_allowed_ingredients()
    ingredients_list = ingredients.lower().split(" ")
    for item in ingredients_list:
        if item.strip(",.") in ingredients_valid:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
