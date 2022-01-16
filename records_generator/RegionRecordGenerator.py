from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class RegionRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.region_id_generator = count(start=0, step=1)
        self.region_names = self.helper.load_file("data/region_names.txt")

    def generate_record(self) -> str:
        self.helper.max_region_id += 1
        return f"INSERT INTO Regions(RegionID, RegionName, CountryID) " + \
               f"VALUES ({next(self.region_id_generator)}, " + \
               f"{choice(self.region_names)}, {randint(0, self.helper.max_country_id)})"
