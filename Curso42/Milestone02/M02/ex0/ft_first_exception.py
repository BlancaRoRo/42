def input_temperature(temp_str: str) -> int:
    value: int = int(temp_str)
    return value


def test_temperature() -> None:
    value: int = 0
    test_list: list[str] = ["25", "abc"]

    print("=== Garden Temperature ===\n")
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
