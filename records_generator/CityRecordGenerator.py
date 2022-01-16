from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class CityRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.city_id_generator = count(start=0, step=1)
        self.city_names = self.helper.load_file("data/city_names.txt")

    def generate_record(self) -> str:
        self.helper.max_city_id += 1
        return f"INSERT INTO Cities(CityID, CityName, RegionID) " + \
               f"VALUES ({next(self.city_id_generator)}, " + \
               f"{choice(self.city_names)}, {randint(0, self.helper.max_region_id)})"
