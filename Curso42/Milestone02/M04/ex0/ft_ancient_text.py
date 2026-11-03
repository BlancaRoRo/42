import sys
import typing

# open() devuelve un objeto archivo de tipo typing.IO[str] (modo texto).
# Sin with hay que cerrarlo a mano: el close() va en un finally para que
# se ejecute aunque read() falle.
# read puede fallar con UnicodeDecodeError (archivo binario, imagen) u
# OSError (desconexión USB, error de disco).

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ft_ancient_text.py <file>")
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(sys.argv[1], "r")
        except OSError as e:
            raise OSError(f"Error opening file '{sys.argv[1]}': {e}") from e
        try:
            content = f.read()
        except (OSError, UnicodeDecodeError) as e:
            raise OSError(f"Error reading file '{sys.argv[1]}': {e}") from e
        finally:
            f.close()
        print("---\n")
        print(f"{content}\n")
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except ValueError as e:
        print(f"{e}")
    except OSError as e:
        print(f"{e}")
