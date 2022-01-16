from RecordGenerator import RecordGenerator
from random import choice, randint
from itertools import count


class RegionRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddRegion"
        self.region_id_generator = count(start=0, step=1)
        self.region_names = self.helper.load_file("data/region_names.txt")

    def generate_record(self) -> str:
        self.helper.max_region_id += 1
        args = [str(next(self.region_id_generator)), choice(self.region_names), 
                str(randint(0, self.helper.max_country_id))]
        return self.make_query(self.procedure_name, args)
