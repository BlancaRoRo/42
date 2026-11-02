import os
from dotenv import load_dotenv

DEFAULTS = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///matrix.db",
    "API_KEY": "",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8000",
}


# Funcionalidad: imprime las variables y sus valores,
# si no están en os.environ imprime el valor por defecto
def env_development() -> None:
    for name, value in DEFAULTS.items():
        if not os.getenv(name):
            print(f"[MISSING] value {name}")
            print(f"Default value for {name}: {value}")
        else:
            print(f"{name}: {os.getenv(name)}")


# Funcionalidad: imprime las variables y sus valores,
# si no están en os.environ imprime el valor por defecto.
# Si es API_KEY imprime *** en cualquier caso
def env_production() -> None:
    for name, value in DEFAULTS.items():
        if not os.getenv(name):
            if name == "API_KEY":
                shown = "***"
            elif name == "LOG_LEVEL":
                shown = "WARNING"
            else:
                shown = value
            print(f"[MISSING] value {name}")
            print(f"Default value for {name}: {shown}")
        else:
            secret = "*********"
            print(f"{name}: "
                  f"{secret if name == 'API_KEY' else os.getenv(name)}")


# Funcionalidad: Comprueba que el .env esté escrito en el .gitignore
def env_is_ignore() -> bool:
    path_git = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(path_git) as f:
            for line in f:
                if line.strip() == ".env":
                    return True
    except OSError:
        print("[INFO] No .gitignore found")
    return False


if __name__ == "__main__":
    # buscamos el .env dentro de esta carpeta
    path = os.path.join(os.path.dirname(__file__), ".env")
    # cargamos las variables de entorno.
    # si no está en UTF-8 o no tiene suficientes permisos da error
    try:
        load_dotenv(path)
    except (OSError, UnicodeDecodeError) as e:
        print(f"[WARNING] Could not load .env: {e}")
    print("ORACLE STATUS: Consulting configuration...")
    print()
    print("Configuration loaded:")
    # para development si está vacío o el valor es development
    mode = os.getenv("MATRIX_MODE")
    if not mode or mode == "development":
        env_development()
    else:
        env_production()
    # Si no hay ninguna contraseña escrita en el archivo
    if DEFAULTS["API_KEY"] == "":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY has a hardcoded default in the code")
    # comprueba que el .env está dentro del .gitignore
    if env_is_ignore():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file not ignored by git, add it to .gitignore")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")
