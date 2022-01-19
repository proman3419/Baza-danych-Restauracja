from RecordGenerator import RecordGenerator
from random import randint
from collections import defaultdict
from itertools import count


class CompanyReservationDetailsRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCompanyReservationDetails"
        self.reservation_table_ids = defaultdict(lambda: count(start=0, step=1))

    def generate_record(self) -> str:
        reservation_id = randint(0, self.helper.max_reservation_id)
        args = [reservation_id,
                next(self.reservation_table_ids[reservation_id]),
                randint(0, 10),
                self.helper.pick_arg_or_null(randint(0, self.helper.max_table_id))]
        return self.make_query(self.procedure_name, args)
