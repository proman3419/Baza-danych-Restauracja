from abc import ABC, abstractmethod


class RecordGenerator(ABC):
    @abstractmethod
    def generate_record(self) -> str:
        raise NotImplementedError

    def make_query(self, header: str, args) -> str:
        return ''.join([header, " VALUES (", ", ".join(map(str, args)), ')'])
