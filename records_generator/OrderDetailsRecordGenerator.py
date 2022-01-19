from RecordGenerator import RecordGenerator
from random import randint
from itertools import count


class OrderDetailsRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddOrderDetails"

    def generate_record(self) -> str:
        args = [randint(0,self.helper.max_order_id),
                randint(0, self.helper.max_menu_item_id),
                randint(0, 10)]
        return self.make_query(self.procedure_name, args)
