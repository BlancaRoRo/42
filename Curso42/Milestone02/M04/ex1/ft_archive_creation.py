import sys
import typing

# se busca el final de línea para añadir un # y meterlo en transformed
# open(, "w") crea un archivo nuevo vacío o vacía uno ya existente
# al final preguntamos si el archivo termina con \n, si no añadimos el #
# write() escribe en un buffer: los datos llegan al disco en close(),
# así que close() también puede fallar y va dentro del try

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: ft_archive_creation.py <file>")
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
        newfile = input("Enter new file name (or empty): ")
        if len(newfile) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{newfile}'")
            try:
                try:
                    new_file: typing.IO[str] = open(newfile, "w")
                except OSError as e:
                    raise OSError(
                        f"Error opening file '{newfile}': {e}") from e
                try:
                    new_file.write(transformed)
                finally:
                    new_file.close()
                print(f"Data saved in file '{newfile}'.")
            except OSError as e:
                print(f"{e}")
                print("Data not saved.")
    except ValueError as e:
        print(f"{e}")
    except OSError as e:
        print(f"{e}")
    except EOFError:
        print("\nEOFError: Unexpected end of file.")
        print("Not saving data.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Process interrupted by user.")
        print("Not saving data.")
