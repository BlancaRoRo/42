def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    match unit:
        case "area":
            real_unit = "square meters"
        case "packets":
            real_unit = "packets available"
        case "grams":
            real_unit = "grams total"
        case _:  # other differents values
            real_unit = "unknown unit"
    print(f"{seed_type.capitalize()} seeds: covers {quantity} {real_unit}")
