from RecordGenerator import RecordGenerator
from random import randint


class TableHistRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddTableHist"

    def generate_record(self) -> str:
        args = [randint(0, self.helper.max_reservation_id), 
                randint(0, self.helper.max_table_id),
                self.helper.get_random_date_str(),
                self.helper.get_random_date_str()] # TODO d1 < d2
        return self.make_query(self.procedure_name, args)
