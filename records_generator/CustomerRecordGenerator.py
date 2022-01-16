from RecordGenerator import RecordGenerator
from itertools import count


class CustomerRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddCustomer"
        self.customer_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_customer_id += 1
        sex = self.helper.get_random_sex()
        args = [next(self.customer_id_generator), 
                self.helper.get_random_phone_nr(),
                self.helper.get_random_email()]
        return self.make_query(self.procedure_name, args)
