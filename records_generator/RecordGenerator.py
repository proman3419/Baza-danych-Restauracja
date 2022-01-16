from abc import ABC, abstractmethod


class RecordGenerator(ABC):
    @abstractmethod
    def generate_record(self) -> str:
        raise NotImplementedError

    def make_query(self, procedure_name: str, args) -> str:
        return ' '.join([procedure_name, ", ".join(map(str, args))])
