# import circular a propósito: dark_validator también importa este módulo
# al principio, así que cargar cualquiera de los dos hace explotar el otro
from .dark_validator import validate_ingredients


# Funcionalidad: devuelve la lista de ingredientes oscuros válidos
def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


# Funcionalidad: Devuelve si el hechizo es rechazado o no basandose en
# validate_ingredients
def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
