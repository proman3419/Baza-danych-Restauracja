from RecordGenerator import RecordGenerator
from itertools import count


class DishCategoryRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddDishCategory"
        self.dish_category_id_generator = count(start=0, step=1)
        self.dish_category_names = self.helper.load_file("data/dish_category_names.txt")

    def generate_record(self) -> str:
        if self.helper.max_dish_category_id < len(self.dish_category_names) - 1:
            self.helper.max_dish_category_id += 1
            args = [next(self.dish_category_id_generator), self.dish_category_names[self.helper.max_dish_category_id]]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty Dish Category record"