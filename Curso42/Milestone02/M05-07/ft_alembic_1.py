# import alchemy ejecuta alchemy/__init__.py y solo da acceso a lo que
# este importa (create_air). create_earth sigue en alchemy/elements.py,
# pero no forma parte de la interfaz del paquete
import alchemy

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    # error de mypy esperado: el enunciado pide que esta llamada falle
    print(alchemy.create_earth())
