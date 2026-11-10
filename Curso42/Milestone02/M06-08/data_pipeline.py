from abc import abstractmethod, ABC
from typing import Any, Protocol


# Cualquier clase con un método con esta cabecera, es una clase de tipo ExportPlugin
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


# Exporta los valores en una línea CSV separada por comas
class CSVExportPlugin:
    # un valor con coma, comillas o salto de línea va entre comillas,
    # y las comillas internas se duplican (regla del formato CSV)
    def _escape(self, value: str) -> str:
        if ',' in value or '"' in value or '\n' in value:
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(self._escape(value))
        print("CSV Output:")
        print(",".join(values))


# Exporta un objeto JSON con claves "item_<rank>"
class JSONExportPlugin:
    # en JSON hay que escapar la barra invertida y las comillas dobles
    def _escape(self, value: str) -> str:
        return value.replace('\\', '\\\\').replace('"', '\\"')

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs: list[str] = []
        for rank, value in data:
            pairs.append(f'"item_{rank}": "{self._escape(value)}"')
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataProcessor(ABC):
    # atributos de clase
    name: str = "Data Processor"

    def __init__(self) -> None:
        # lista de tuplas (rank, dato en str), donde se almacenan
        self._storage: list[tuple[int, str]] = []
        # contador para saber el índice
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # pass = vacío. Para que python sepa cuando termina el método
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # número de datos que quedan guardados (baja con output)
    def len_storage(self) -> int:
        return len(self._storage)

    # número total de datos procesados (nunca baja)
    def get_counter(self) -> int:
        return self._counter

    # guarda un dato ya convertido a str con su rank
    def _store(self, value: str) -> None:
        self._storage.append((self._counter, value))
        self._counter += 1

    # saca el dato más antiguo (posición 0) y lo elimina de la lista
    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

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
    name: str = "Text Processor"

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
    name: str = "Log Processor"

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


class DataStream:
    def __init__(self) -> None:
        self._dataProcessor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        for processor in self._dataProcessor:
            if type(processor) is type(proc):
                return
        self._dataProcessor.append(proc)

    # Polimorfismo: llama a validate de la clase que estas usando.
    # Elige a qué procesador ir y si ninguno lo gestiona devuelve el print
    def process_stream(self, stream: list[Any]) -> None:
        flag: int = 0
        for item in stream:
            flag = 0
            for processor in self._dataProcessor:
                if processor.validate(item):
                    processor.ingest(item)
                    flag = 1
                    break
            if flag == 0:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    # Funcionalidad: Te imprime el número total de items guardados
    # (counter) y los que actualmente estan guardados (len de storage)
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._dataProcessor) == 0:
            print("No processor found, no data")
            return
        for processor in self._dataProcessor:
            print(f"{processor.name}: "
                  f"total {processor.get_counter()} items processed, "
                  f"remaining {processor.len_storage()} on processor")

    # Consume hasta nb datos de cada procesador y se los pasa al plugin.
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._dataProcessor:
            list_output: list[tuple[int, str]] = []
            # si quedan menos de nb, se sacan solo los que hay
            for _ in range(min(nb, processor.len_storage())):
                list_output.append(processor.output())
            if list_output:
                plugin.process_output(list_output)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    first_batch: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {first_batch}\n")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    print()
    data_stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'},
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print(f"\nSend another batch of data: {second_batch}\n")
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    print()
    data_stream.print_processors_stats()
