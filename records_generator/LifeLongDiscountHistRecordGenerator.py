from RecordGenerator import RecordGenerator
from random import randint, uniform


class LifeLongDiscountHistRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddLifeLongDiscountHist"

    def generate_record(self) -> str:
        args = [randint(0, 20), randint(0, 20), round(uniform(0.01, 0.5), 2), self.helper.get_random_date_str(),
                self.helper.get_random_date_str()]
        return self.make_query(self.procedure_name, args)
