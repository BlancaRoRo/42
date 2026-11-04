# bin/python enlace simbólico al python del sistema
# pyvenv.cfg archivo con: ruta del ejecutable central,
# versión python, si hay o no carpeta de paquetes
import sys
import os
import site


def print_out() -> None:
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows")
    print("Then run this program again")


def print_in() -> None:
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    # ultima palabra de la ruta a la carpeta, osea, el nombre del entorno
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print(f"Reagent installation path: {site.getsitepackages()[0]}")


if __name__ == "__main__":
    # es un entorno ?
    if sys.prefix != sys.base_prefix:
        print_in()
    else:
        print_out()
