import sys
import typing

# sys.stdout: salida normal, aquí el mensaje para que el usuario responda
# sys.stdin: entrada de datos desde el teclado del usuario
# sys.stderr: salida de errores, separada de la normal
# flush() fuerza a que el prompt se muestre antes de esperar la respuesta
# readline() devuelve "" en EOF (ctrl+D) y "\n" si solo se pulsa Enter


def input_data(message: str) -> str:
    sys.stdout.write(message)
    sys.stdout.flush()
    line = sys.stdin.readline()
    if line == "":
        sys.stdout.write("\n")
    return line.rstrip("\n")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ft_stream_management.py <file>")
        print("=== Cyber Archives Recovery & Preservation ===")
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
        print(f"File '{sys.argv[1]}' closed.\n")
        print("Transform data:")
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
        newfile = input_data("Enter new file name (or empty): ")
        if len(newfile) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{newfile}'")
            try:
                new_file: typing.IO[str] = open(newfile, "w")
                try:
                    new_file.write(transformed)
                finally:
                    new_file.close()
                print(f"Data saved in file '{newfile}'.")
            except OSError as e:
                print("[STDERR] Error opening file "
                      f"'{newfile}': {e}", file=sys.stderr)
                print("Data not saved.")
    except ValueError as e:
        print(f"[STDERR] {e}", file=sys.stderr)
        sys.stderr.flush()
    except OSError as e:
        print(f"[STDERR] {e}", file=sys.stderr)
        sys.stderr.flush()
    except KeyboardInterrupt:
        print("[STDERR] KeyboardInterrupt:"
              "Process interrupted by user.", file=sys.stderr)
        print("Not saving data.")
        sys.stderr.flush()
