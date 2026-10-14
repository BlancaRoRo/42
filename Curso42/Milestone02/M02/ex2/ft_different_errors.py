# El comentario de "type" se pone para que mypy no salte con el error.
# Ese error se pone a propósito para el test. Evidentemente no se puede
# sumar un str y un int.


def garden_operations(operation_number: int) -> None:
    string: str = ""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        100/0
    elif operation_number == 2:
        open("usr/noexist/file.txt")
    elif operation_number == 3:
        string += 3  # type: ignore[operator]


def test_error_types() -> None:
    test_list: list[int] = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")
    for i in test_list:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()
    for i in test_list:
        print(f"Testing multiple errors {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught an error: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
