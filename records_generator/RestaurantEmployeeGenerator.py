from RecordGenerator import RecordGenerator
from random import randint
from itertools import count


class RestaurantEmployeeGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddRestaurantEmployee"
        self.restaurant_employee_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_restaurant_employee_id += 1
        sex = self.helper.get_random_sex()
        args = [next(self.restaurant_employee_id_generator), 
                self.helper.get_random_first_name(sex),
                self.helper.get_random_last_name(sex),
                self.helper.get_random_phone_nr(),
                self.helper.get_random_email(),
                str(randint(0, self.helper.max_city_id))]
        return self.make_query(self.procedure_name, args)
