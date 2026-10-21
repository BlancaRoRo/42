import sys


# sys.argv[] lista []. Sirve para leer los datos de entrada del main

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        count: int = 1
        for i in sys.argv[1:]:
            print(f"Argument {count}: {i}")
            count += 1
    print(f"Total arguments: {len(sys.argv)}")
