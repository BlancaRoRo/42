import sys
import typing

# se busca el final de línea para añadir un # y meterlo en transformed
# open(, "w") te crea un nuevo archivo vacio para escribir o te vacía uno ya existente para escribir
# al final preguntamos si el final del archivo termina con \n, sino añadimos el #

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
        newfile = input("Enter new file name (or empty):") 
        if len(newfile) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{newfile}'")
            new_file = open(newfile, "w")
            new_file.write(transformed)
            new_file.close()
            print(f"Data saved in file '{newfile}'")
    except ValueError as e:
        print(f"{e}")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
