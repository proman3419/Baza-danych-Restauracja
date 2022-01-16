from RecordGeneratorHelper import RecordGeneratorHelper as RGH
from RecordGenerator import RecordGenerator
from random import choice, randint


class CompanyRecordGenerator(RecordGenerator):
    def __init__(self):
        self.last_customer_id = -1
        self.company_names = ["Drutex", "Nokia", "Budowlanex", "Akamai", "Nissan"]
        self.addresses = ["Pawia", "Krakowska", "Warszawska", "Mazowiecka", "Wiślicka"]
        self.nip = 10**9

    def generate_record(self) -> str:
        if self.last_customer_id < RGH.max_customer_id:
            self.last_customer_id += 1
            self.nip += 1
            return f"INSERT INTO Companies(CustomerID, CompanyName, Address, " + \
                   f"CityID, PostalCode, NIP) " + \
                   f"VALUES ({self.last_customer_id}, " + \
                   f"{choice(self.company_names)}, " + \
                   f"{choice(self.addresses)}, " + \
                   f"{randint(0, RGH.max_city_id)}, " + \
                   f"{RGH.get_random_numeral_str(5)}, " + \
                   f"{self.nip})"
        else:
            return "--Empty Company record"
