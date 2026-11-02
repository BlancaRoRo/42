import os
import importlib
import importlib.metadata


# diccinario con descripción que se muestra junto a cada reagent
DESCRIPTIONS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def read_requirements(path: str) -> list[str]:
    # devuelve los nombres de los paquetes declarados en requirements.txt
    packages = []
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                # guarda caracteres mientras sean válidos en un nombre
                # "pandas>=2.0" -> "pandas"
                name = ""
                for char in line:
                    if char.isalnum() or char in "-_.":
                        name += char
                    else:
                        break
                packages.append(name)
    except OSError as e:
        print(f"Could not read {path}: {e}")
    return packages


def check_reagent(package: str) -> bool:
    # Devuelve el par con la clave package y sino devuelve ready
    description = DESCRIPTIONS.get(package, "ready")
    try:
        # lee la versión de los metadatos (carpeta *.dist-info)
        version = importlib.metadata.version(package)
        # importa el paquete para comprobar que funciona de verdad
        importlib.import_module(package)
    except importlib.metadata.PackageNotFoundError:
        print(f"[MISSING] {package} - not installed")
        return False
    except ImportError as e:
        print(f"[ERROR] {package} ({version}) - cannot be imported: {e}")
        return False
    print(f"[OK] {package} ({version}) - {description}")
    return True


def print_pip_vs_poetry() -> None:
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins "
          "the resolved")
    print("versions in poetry.lock so every install is identical.")


def print_install_help(missing: list[str]) -> None:
    # join une los elementos de una lista con ,: numpy, pandas etc..
    print(f"Missing reagents: {', '.join(missing)}")
    print("To install them with pip:")
    print("    pip install -r ex0/requirements.txt")
    print("    python3 ex0/loading.py")
    print("To install them with Poetry:")
    print("    poetry install")
    print("    poetry run python ex0/loading.py")


if __name__ == "__main__":
    # une la carpeta del script actual (sacada de __file__)
    # con el nombre del archivo requirements.txt
    path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    packages = read_requirements(path)
    missing = []
    for package in packages:
        if not check_reagent(package):
            missing.append(package)
    print()
    print_pip_vs_poetry()
    print()
    # si hay algún paquete que no se ha instalado
    # mostrar texto con dichos paquetes
    if missing:
        print_install_help(missing)
    elif packages:
        print("All reagents present and accounted for.")
    else:
        print("No reagents declared in requirements.txt.")
