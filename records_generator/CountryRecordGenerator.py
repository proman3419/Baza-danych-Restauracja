from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class CountryRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCountry"
        self.country_id_generator = count(start=0, step=1)
        self.country_names = self.helper.load_file("data/country_names.txt")

    def generate_record(self) -> str:
        self.helper.max_country_id += 1
        args = [str(next(self.country_id_generator)), choice(self.country_names)]
        return self.make_query(self.procedure_name, args)
