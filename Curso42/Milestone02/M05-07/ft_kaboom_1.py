if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    # el import va aquí y no arriba para que los print salgan antes de
    # que explote el import circular
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Necromancy", "bats and frogs"))
