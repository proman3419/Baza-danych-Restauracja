from RecordGenerator import RecordGenerator
from random import randint
from itertools import count


class DiscountRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddDiscount"
        self.discount_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_discount_id += 1
        args = [next(self.discount_id_generator),
                randint(0, self.helper.max_customer_id)]
        return self.make_query(self.procedure_name, args)
