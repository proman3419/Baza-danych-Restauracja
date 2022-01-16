from abc import ABC, abstractmethod


class RecordGenerator(ABC):
    @abstractmethod
    def generate_record(self) -> str:
        raise NotImplementedError
