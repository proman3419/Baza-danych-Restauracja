from RecordGenerator import RecordGenerator
from random import randint


class TableHistRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddTableHist"

    def generate_record(self) -> str:
        date1, date2 = self.helper.get_random_dates_pair_str()
        args = [randint(0, self.helper.max_reservation_id), 
                randint(0, self.helper.max_table_id),
                date1, date2]
        return self.make_query(self.procedure_name, args)
