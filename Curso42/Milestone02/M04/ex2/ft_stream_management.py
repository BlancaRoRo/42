import sys
import typing

# sys.stdout se usa para la salida de la terminal: en este caso el mensaje para que el usuario responda
# sys.stdin se usa para capturar la entrada: la entrada de datos desde el teclado del usuario
# sys.exit(1) es la salida de errores inmediata. Se usa 1 por convención de error, 0 sería todo correcto.
def input_data(message: str) -> str:
    sys.stdout.write(message)
    sys.stdout.flush()
    line = sys.stdin.readline()
    if line == " ":
        sys.stderr.write("Empty line")
        sys.exit(1)
    return line.strip()
    
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
        print(f"File '{sys.argv[1]}' closed.\n")
        print("Trafnsform data:")
        print("---\n")
        transformed = ""
        i = 0
        total_characters = len(content)

        while i < total_characters:
            current = content[i]
            if current == '\n':
                transformed = transformed + "#\n"
            else:
                transformed = transformed + current
            i += 1
        if total_characters > 0 and content[total_characters - 1] != '\n':
            transformed = transformed + "#\n"
        print(f"{transformed}")
        print("---")
        newfile = input_data("Enter new file name (or empty):") 
        if len(newfile) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{newfile}'")
            new_file = open(newfile, "w")
            new_file.write(transformed)
            new_file.close()
            print(f"Data saved in file '{newfile}'")
    except ValueError as e:
        print(f"[STDERR] {e}", file=sys.stderr)
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)