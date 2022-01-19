from RecordGenerator import RecordGenerator
from itertools import count
from random import randint, uniform, choice


class EmployeeRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddEmployee"
        self.max_customer_id = -1

    def generate_record(self) -> str:
        if self.max_customer_id < self.helper.max_customer_id:
            self.max_customer_id += 1
            sex = self.helper.get_random_sex()

            args = [self.max_customer_id, self.helper.get_random_first_name(sex),
                    self.helper.get_random_last_name(sex), randint(0, self.helper.max_customer_id)]
            return self.make_query(self.procedure_name, args)
        else:
            "--Empty Employee record"
