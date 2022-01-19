from RecordGenerator import RecordGenerator
from random import randint


class CompanyReservationRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCompanyReservation"
        self.max_reservation_id = -1

    def generate_record(self) -> str:
        if self.max_reservation_id < self.helper.max_reservation_id:
            self.max_reservation_id += 1
            args = [self.max_reservation_id,
                    randint(0, self.helper.max_customer_id)]
            return self.make_query(self.procedure_name, args)
        else:
            "--Empty CompanyReservation record"
