from RecordGenerator import RecordGenerator
from random import randint, uniform


class SingleUseDiscountHistRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddSingleUseHistDiscountHist"

    def generate_record(self) -> str:
        args = [randint(500, 2000), round(uniform(0.01, 0.5), 2), randint(1, 21), self.helper.get_random_date_str(),
                self.helper.get_random_date_str()]
        return self.make_query(self.procedure_name, args)
