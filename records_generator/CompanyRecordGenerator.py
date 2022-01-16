from RecordGenerator import RecordGenerator
from random import choice, randint


class CompanyRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.header = f"INSERT INTO Companies(CustomerID, CompanyName, Address, CityID, PostalCode, NIP)"
        self.last_customer_id = -1
        self.company_names = self.helper.load_file("data/company_names.txt")
        self.addresses = self.helper.load_file("data/addresses.txt")
        self.nip = 10**9

    def generate_record(self) -> str:
        if self.last_customer_id < self.helper.max_customer_id:
            self.last_customer_id += 1
            self.nip += 1
            args = [self.last_customer_id, choice(self.company_names), choice(self.addresses),
                    randint(0, self.helper.max_city_id),
                    self.helper.get_random_numeral_str(5),
                    self.nip]
            return self.make_query(self.header, args)
        else:
            return "--Empty Company record"
