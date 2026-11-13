from abc import abstractmethod, ABC
from typing import Any, Protocol


# Any class with a method with this signature
# is an ExportPlugin-type class
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


# Exports the values as a comma-separated CSV line
class CSVExportPlugin:
    # a value with a comma, quotes or newline goes inside quotes,
    # and inner quotes are doubled (CSV format rule)
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


# Exports a JSON object with keys "item_<rank>"
class JSONExportPlugin:
    # in JSON, backslashes and double quotes must be escaped
    def _escape(self, value: str) -> str:
        return value.replace('\\', '\\\\').replace('"', '\\"')

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs: list[str] = []
        for rank, value in data:
            pairs.append(f'"item_{rank}": "{self._escape(value)}"')
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataProcessor(ABC):
    # class attributes
    name: str = "Data Processor"

    def __init__(self) -> None:
        # list of tuples (rank, data as str), where they are stored
        self._storage: list[tuple[int, str]] = []
        # counter to keep track of the index
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # pass = empty. So Python knows where the method ends
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # number of items still stored (decreases with output)
    def len_storage(self) -> int:
        return len(self._storage)

    # total number of items processed (never decreases)
    def get_counter(self) -> int:
        return self._counter

    # stores an item already converted to str with its rank
    def _store(self, value: str) -> None:
        self._storage.append((self._counter, value))
        self._counter += 1

    # takes the oldest item (position 0) and removes it from the list
    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

    # @abstractmethod is not used because these are concrete classes
    # and the method becomes a concrete method
    def _is_number(self, item: Any) -> bool:
        # bool inherits from int, so it is checked
        return isinstance(item, (int, float)) and not isinstance(item, bool)

    # accepts a single number or a list of numbers (mixed is fine)
    def validate(self, data: Any) -> bool:
        if self._is_number(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not self._is_number(item):
                    return False
            return True
        return False

    # validates, converts each number to str and stores it separately
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if not isinstance(data, list):
            data = [data]  # Convert the data into a list to iterate
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

    # Functionality: checks that it is a string
    def _is_str(self, item: Any) -> bool:
        return isinstance(item, (str))

    # Functionality: checks that it is a list of dictionaries
    def _is_log(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, dict):
                    return False
            return True
        return False

    # Functionality: accepts a dictionary, which it converts to a list
    # so it can be validated. Checks that the keys/values of the
    # dictionary are strings or contain 'log' in the key
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

    # Functionality: validates the dictionary or list of dictionaries.
    # Converts the dictionary to a list to iterate and store it
    # in the storage
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

    # Polymorphism: calls validate of the class you are using.
    # Chooses which processor to use; if none handles it, prints a message
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

    # Functionality: prints the total number of items stored
    # (counter) and those currently stored (len of storage)
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._dataProcessor) == 0:
            print("No processor found, no data")
            return
        for processor in self._dataProcessor:
            print(f"{processor.name}: "
                  f"total {processor.get_counter()} items processed, "
                  f"remaining {processor.len_storage()} on processor")

    # Consumes up to nb items from each processor and passes them to plugin.
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._dataProcessor:
            list_output: list[tuple[int, str]] = []
            # if fewer than nb remain, only the available ones are taken
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
