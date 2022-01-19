from abc import ABC, abstractmethod


class RecordGenerator(ABC):
    @abstractmethod
    def generate_record(self) -> str:
        raise NotImplementedError

    def make_query(self, procedure_name: str, args) -> str:
        def arg_to_query_arg(arg):
            if type(arg) == str: return f"'{arg}'"
            else: return str(arg)
        return ' '.join(["exec", procedure_name, ", ".join(map(arg_to_query_arg, args))])
