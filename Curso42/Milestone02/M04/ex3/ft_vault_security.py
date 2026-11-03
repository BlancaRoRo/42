# with llama a close() automáticamente al salir del bloque, aunque haya
# un return o salte una excepción dentro (es un try/finally implícito)


def secure_archive(name_file: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, f"Invalid action '{action}': use 'r' or 'w'")
    try:
        with open(name_file, action) as f:
            if action == "r":
                return (True, f.read())
            f.write(content)
        return (True, "Content successfully written to file")
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))
