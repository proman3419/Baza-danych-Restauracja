from RecordGenerator import RecordGenerator
from random import randint
from itertools import count


class ReservationRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddReservation"
        self.reservation_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_reservation_id += 1
        args = [next(self.reservation_id_generator), 
                self.helper.get_random_date_str(),
                randint(0, self.helper.max_restaurant_employee_id)]
        return self.make_query(self.procedure_name, args)
