import sys

# Funcionalidad: Pasa el inventario de cada jugador como argumento y
# calcula estadísticas
if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for i in sys.argv[1:]:
        # Validación de formato
        if i.count(":") != 1:
            print(f"Error - invalid parameter '{i}'")
            continue
        name, value = i.split(":")
        if name == "":
            print(f"Error - invalid parameter '{i}'")
            continue
        # Repetición de item
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        # Conversión de value a int
        try:
            int_value = int(value)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        # Validación de la cantidad: tiene que ser positiva
        if int_value <= 0:
            print(f"Quantity error for '{name}': must be positive")
            continue
        inventory[name] = int_value
    # Si no hay ningún valor válido, no se hace el análisis
    if not inventory:
        print("No valid items provided. Usage: python3 ft_inventory_system.py "
              "<item1>:<quantity1> <item2>:<quantity2> ...")
    else:
        print(f"Got inventory: {inventory}")
        total: int = sum(inventory.values())
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)} items: {total}")
        for item in inventory:
            print(f"Item {item} represents "
                  f"{round(inventory[item] / total * 100, 1)}%")
        # En caso de empate, se queda el primero
        max_qty: int = 0
        min_qty: int = 0
        name_max: str = ""
        name_min: str = ""
        for item in inventory:
            if name_min == "" or inventory[item] < min_qty:
                min_qty = inventory[item]
                name_min = item
            if inventory[item] > max_qty:
                max_qty = inventory[item]
                name_max = item
        print(f"Item most abundant: {name_max} with quantity {max_qty}")
        print(f"Item least abundant: {name_min} with quantity {min_qty}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
