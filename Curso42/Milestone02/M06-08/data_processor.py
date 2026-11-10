from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        # lista de tuplas (rank, dato en str), donde se almacenan
        self._storage: list[tuple[int, str]] = []
        # rank del siguiente dato que se guarde; nunca baja
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # pass = vacío. Para que python sepa cuando termina el método
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # guarda un dato ya convertido a str con su rank
    def _store(self, value: str) -> None:
        self._storage.append((self._counter, value))
        self._counter += 1

    # saca el dato más antiguo (posición 0) y lo elimina de la lista
    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    # no se pone @abstractmethod porque son clases concretas
    # y el método se convierte en un método concreto
    def _is_number(self, item: Any) -> bool:
        # bool hereda de int, se comprueba
        return isinstance(item, (int, float)) and not isinstance(item, bool)

    # acepta un número suelto o una lista de números (mezclados vale)
    def validate(self, data: Any) -> bool:
        if self._is_number(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not self._is_number(item):
                    return False
            return True
        return False

    # valida, convierte cada número a str y lo guarda por separado
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if not isinstance(data, list):
            data = [data]  # Convertir el dato en una lista para iterar
        for item in data:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def _is_str(self, item: Any) -> bool:
        return isinstance(item, str) and item.strip() != ""

    def validate(self, data: Any) -> bool:
        if self._is_str(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not self._is_str(item):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if not isinstance(data, list):
            data = [data]
        for item in data:
            self._store(item)


class LogProcessor(DataProcessor):
    # Funcionalidad: comprueba que sea un string
    def _is_str(self, item: Any) -> bool:
        return isinstance(item, (str))

    # Funcionalidad: comprueba que sea una lista de diccionarios
    def _is_log(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, dict):
                    return False
            return True
        return False

    # Funcionalidad: acepta un diccionario que convierte a lista
    # para poder validarlo. Comprueba que las claves/valor del
    # diccionario sean string o contengan 'log' en la clave
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            data = [data]
        if self._is_log(data):
            for item in data:
                for key, value in item.items():
                    if (not self._is_str(key) or not self._is_str(value)
                            or 'log' not in key):
                        return False
            return True
        return False

    # Funcionalidad: valida el diccionario o lista de diccionarios.
    # Convierte el diccionario a lista para iterar y guardarlo
    # en el storage
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if not isinstance(data, list):
            data = [data]
        for item in data:
            self._store(": ".join(item.values()))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")
    numeric_processor = NumericProcessor()
    print(f"Trying to validate input '42': {numeric_processor.validate(42)}")
    print("Trying to validate input 'Hello':",
          numeric_processor.validate('Hello'))
    try:
        print("Test invalid ingestion of string 'foo' "
              "without prior validation:")
        numeric_processor.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in [0, 1, 2]:
        rank, value = numeric_processor.output()
        print(f"Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print("Trying to validate input '42':", text_processor.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_processor.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    rank, value = text_processor.output()
    print(f"Text value {rank}: {value}")
    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print("Trying to validate input 'Hello':", log_processor.validate("Hello"))
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]
    print(f"Processing data: {logs}")
    log_processor.ingest(logs)
    print("Extracting 2 values...")
    for i in [0, 1]:
        rank, value = log_processor.output()
        print(f"Log entry {rank}: {value}")
