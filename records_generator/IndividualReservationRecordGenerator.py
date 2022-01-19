from RecordGenerator import RecordGenerator
from random import randint, choice


class IndividualReservationRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddIndividualReservation"
        self.methods_of_payment = self.helper.load_file("data/methods_of_payment.txt")
        self.max_reservation_id = -1

    def generate_record(self) -> str:
        if self.max_reservation_id < self.helper.max_reservation_id:
            self.max_reservation_id += 1
            args = [self.max_reservation_id,
                    randint(0, self.helper.max_table_id),
                    randint(0, self.helper.max_order_id),
                    choice(self.methods_of_payment)]
            return self.make_query(self.procedure_name, args)
        else:
            "--Empty IndividualReservation record"
