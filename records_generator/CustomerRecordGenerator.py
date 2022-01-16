from RecordGeneratorHelper import RecordGeneratorHelper as RGH
from RecordGenerator import RecordGenerator
from itertools import count


class CustomerRecordGenerator(RecordGenerator):
    def __init__(self):
        self.customer_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        RGH.max_customer_id += 1
        sex = RGH.get_random_sex()
        return f"INSERT INTO Customers(CustomerID, Phone, Email) " + \
               f"VALUES ({next(self.customer_id_generator)}, " + \
               f"{RGH.get_random_phone_nr()}, " + \
               f"{RGH.get_random_email()})"
