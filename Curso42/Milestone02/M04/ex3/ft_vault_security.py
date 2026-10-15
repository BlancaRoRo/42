def secure_archive(name_file: str, action: str = "r", content: str = "") -> tuple[bool, str]:
    if action != "r" or action != "w":
        return (False, f"Invalid action '{action}': use 'r' or 'w'")
    try:
        with open(name_file, action) as f:
            if action == "r":
                return (True, f.read())
            f.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
            return (False, str(e))

if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    secure_archive("/not/existing/fil")
    print("Using 'secure_archive' to read from an inaccessible file:")
    secure_archive("etc/master.passwd")
    print("Using 'secure_archive' to read from a regular file:")
    secure_archive("archivo.txt", "[FRAGMENT 001] Digital preservation protocols established 2087\n[FRAGMENT 002] Knowledge must survive the entropy wars\n[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    secure_archive("archivo.txt", "nuevo contenido")
