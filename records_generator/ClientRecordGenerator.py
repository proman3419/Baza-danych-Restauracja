from RecordGeneratorHelper import RecordGeneratorHelper as RGH
from RecordGenerator import RecordGenerator


class ClientRecordGenerator(RecordGenerator):
    def __init__(self):
        self.last_customer_id = -1

    def generate_record(self) -> str:
        if self.last_customer_id < RGH.max_customer_id:
            self.last_customer_id += 1
            sex = RGH.get_random_sex()
            return f"INSERT INTO Clients(CustomerID, FirstName, LastName) " + \
                   f"VALUES ({self.last_customer_id}, " + \
                   f"{RGH.get_random_first_name(sex)}, " + \
                   f"{RGH.get_random_last_name(sex)})"
        else:
            return "--Empty Client record"
