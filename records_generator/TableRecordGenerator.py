from RecordGenerator import RecordGenerator
from random import randint
from itertools import count


class TableRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddTable"
        self.table_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_table_id += 1
        args = [next(self.table_id_generator), randint(1, 10)]
        return self.make_query(self.procedure_name, args)
