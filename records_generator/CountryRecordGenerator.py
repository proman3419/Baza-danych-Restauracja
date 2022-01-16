from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class CountryRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.country_id_generator = count(start=0, step=1)
        self.country_names = self.helper.load_file("data/country_names.txt")

    def generate_record(self) -> str:
        self.helper.max_country_id += 1
        return f"INSERT INTO Countries(CountryID, CountryName) " + \
               f"VALUES ({next(self.country_id_generator)}, " + \
               f"{choice(self.country_names)})"
