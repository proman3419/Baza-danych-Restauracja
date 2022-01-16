from RecordGeneratorHelper import RecordGeneratorHelper as RGH
from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class RegionRecordGenerator(RecordGenerator):
    def __init__(self):
        self.region_id_generator = count(start=0, step=1)
        self.region_names = ["Małopolska", "Mazowieckie", "Wielkopolska"]

    def generate_record(self) -> str:
        RGH.max_region_id += 1
        return f"INSERT INTO Regions(RegionID, RegionName, CountryID) " + \
               f"VALUES ({next(self.region_id_generator)}, {choice(self.region_names)}, {randint(0, RGH.max_country_id)})"
