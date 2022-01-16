from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class CityRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCity"
        self.city_id_generator = count(start=0, step=1)
        self.city_names = self.helper.load_file("data/city_names.txt")

    def generate_record(self) -> str:
        self.helper.max_city_id += 1
        args = [next(self.city_id_generator), choice(self.city_names), 
                randint(0, self.helper.max_region_id)]
        return self.make_query(self.procedure_name, args)
