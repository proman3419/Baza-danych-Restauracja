from RecordGenerator import RecordGenerator
from itertools import count
from random import randint, uniform


class MenuItemRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddMenuItem"
        self.menu_item_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_menu_item_id += 1
        date1, date2 = self.helper.get_random_dates_pair_str()
        args = [next(self.menu_item_id_generator), 
                randint(0, self.helper.max_dish_id), round(uniform(0.0, 150.0),2),
                date1, self.helper.pick_arg_or_null(date2)]
        return self.make_query(self.procedure_name, args)