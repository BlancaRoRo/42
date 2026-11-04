# solo se expone el grimorio light: si aquí se importara dark_spellbook,
# cualquier "import alchemy.grimoire" explotaría por el import circular
from .light_spellbook import light_spell_record

__all__ = ["light_spell_record"]
