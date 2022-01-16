from RecordGenerator import RecordGenerator
from itertools import count


class CustomerRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.customer_id_generator = count(start=0, step=1)

    def generate_record(self) -> str:
        self.helper.max_customer_id += 1
        sex = self.helper.get_random_sex()
        return f"INSERT INTO Customers(CustomerID, Phone, Email) " + \
               f"VALUES ({next(self.customer_id_generator)}, " + \
               f"{self.helper.get_random_phone_nr()}, " + \
               f"{self.helper.get_random_email()})"
