# bin/python enlace simbólico al python del sistema
# pyvenv.cfg archivo con: ruta del ejecutable central,
# versión python, si hay o no carpeta de paquetes
# sys info del intérprete python
# os info del sistema operativo
# te da info de los paquetes de python instalados (también están en sys)
# pero habría que filtrarlos
import sys
import os
import site


def print_out() -> None:
    print("LABORATORY STATUS: You are working in the open")
    # archivo en el que se está ejeutando el intérprete
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
    # ultima palabra de la ruta a la carpeta del entorno
    # osea, el nombre del entorno
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    # devuelve una lista con la ruta de los paquetes
    print(f"Reagent installation path: {site.getsitepackages()[0]}")


if __name__ == "__main__":
    # es un entorno ?
    # compara la ruta de la carpeta de python que se está ejecutando (venv)
    # con la carpeta donde está instalado python en el sistema (/usr)
    if sys.prefix != sys.base_prefix:
        print_in()
    else:
        print_out()
