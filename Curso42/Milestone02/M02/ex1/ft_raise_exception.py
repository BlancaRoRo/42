def input_temperature(temp_str: str) -> int:
    value: int = int(temp_str)
    if value > 40:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")
    elif value < 0:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
    return value


def test_temperature() -> None:
    test_list: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for temp_str in test_list:
        try:
            print(f"Input data is '{temp_str}'")
            value = input_temperature(temp_str)
            print(f"Temperature is now {value}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
