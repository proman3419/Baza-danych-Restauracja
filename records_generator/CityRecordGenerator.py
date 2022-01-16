from RecordGeneratorHelper import RecordGeneratorHelper as RGH
from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class CityRecordGenerator(RecordGenerator):
    def __init__(self):
        self.city_id_generator = count(start=0, step=1)
        self.city_names = ["Warszawa", "Kraków", "Lublin", "Londyn", "Paryż", "Tokio", "Przemyśl"]

    def generate_record(self) -> str:
        RGH.max_city_id += 1
        return f"INSERT INTO Cities(CityID, CityName, RegionID) " + \
               f"VALUES ({next(self.city_id_generator)}, {choice(self.city_names)}, {randint(0, RGH.max_region_id)})"
