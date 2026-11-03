from .light_validator import validate_ingredients
# Funcionalidad: devuelve la lista de ingredientes válidos
def light_spell_allowed_ingredients() -> list[str]:
    return ingredients = ["earth", "air", "fire", "water"]


# Funcionalidad: Devuelve si el hechizo es rechazado o no basandose en 
# validate_ingredients
def light_spell_record(spell_name: str, ingredients: str) -> bool:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"