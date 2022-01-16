from RecordGenerator import RecordGenerator
from random import choice, randint


class CompanyRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.last_customer_id = -1
        self.company_names = self.helper.load_file("data/company_names.txt")
        self.addresses = self.helper.load_file("data/addresses.txt")
        self.nip = 10**9

    def generate_record(self) -> str:
        if self.last_customer_id < self.helper.max_customer_id:
            self.last_customer_id += 1
            self.nip += 1
            return f"INSERT INTO Companies(CustomerID, CompanyName, Address, " + \
                   f"CityID, PostalCode, NIP) " + \
                   f"VALUES ({self.last_customer_id}, " + \
                   f"{choice(self.company_names)}, " + \
                   f"{choice(self.addresses)}, " + \
                   f"{randint(0, self.helper.max_city_id)}, " + \
                   f"{self.helper.get_random_numeral_str(5)}, " + \
                   f"{self.nip})"
        else:
            return "--Empty Company record"
