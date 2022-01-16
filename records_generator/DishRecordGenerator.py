from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class DishRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddDish"
        self.dish_id_generator = count(start=0, step=1)
        self.dish_names = self.helper.load_file("data/dish_names.txt")

    def generate_record(self) -> str:
        if self.helper.max_dish_id < len(self.dish_names) - 1:
            self.helper.max_dish_id += 1
            args = [next(self.dish_id_generator), self.dish_names[self.helper.max_dish_id],
                    randint(0, self.helper.max_dish_category_id)]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty Dish record"
