from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    # readable name; each subclass overrides it with its own
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


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)
    list_stream: list[Any] = [
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
    print(f"Send first batch of data on stream: {list_stream}")
    data_stream.process_stream(list_stream)
    data_stream.print_processors_stats()
    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    print("Send the same batch again")
    data_stream.process_stream(list_stream)
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for i in [0, 1, 2]:
        numeric.output()
    for i in [0, 1]:
        text.output()
    for i in [0]:
        log.output()
    data_stream.print_processors_stats()
