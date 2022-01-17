from RecordGenerator import RecordGenerator
from random import randint


class CompanyEmployeeReservationDetailsRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCompanyEmployeeReservationDetails"

    def generate_record(self) -> str:
        args = [randint(0, self.helper.max_reservation_id),
                randint(0, self.helper.max_customer_id),
                randint(0, self.helper.max_table_id)]
        return self.make_query(self.procedure_name, args)
