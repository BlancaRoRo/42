import sys
import typing

# with open(, "r") se usa para cerrar el archivo automáticamente 
# por si hay algún error que no lo deje terminar
#  la r significa read y se puede usar tambien w o x.

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ft_ancient_text.py <file>")
        print("=== Cyber Archives Recovery ===")
        print(f"Accesing file '{sys.argv[1]}'")
        with open(sys.argv[1], "r") as f:
            content = f.read()
        print("---\n")
        print(f"{content}\n")
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except ValueError as e:
        print(f"{e}")
    except FileNotFoundError:
        print(f"Error opening file '{sys.argv[1]}'"
        f": [Errno 2] No such file or directory: '{sys.argv[1]}'")
    except PermissionError:
        print(f"Error opening file '{sys.argv[1]}':"
         f"[Errno 13] Permission denied: '{sys.argv[1]}'")

