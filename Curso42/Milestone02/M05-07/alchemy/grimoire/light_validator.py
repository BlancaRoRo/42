
# Funcionalidad: Devuelve si el hechizo es válido si algún ingrediente está contenido
# en los ingredientes válidos
# al poner el import dentro del método, carga primero validate_ingredients que su
# dependencia
# import .light_spellbook también valdría. Si importo el módulo solo necesita 
# que esté cargado el módulo no la función, por lo que no habría problemas
# al haberse inicializado antes.
def  validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingredients_valid = light_spell_allowed_ingredients()
    ingredients_list = ingredients.lower().split(" ")
    for item in ingredients_list:
        if item in ingredients_valid:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
