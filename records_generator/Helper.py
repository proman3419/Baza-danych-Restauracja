from random import choice, randint
from string import ascii_lowercase
from typing import List
from os import sep


class Helper:
    def __init__(self):
        self.max_city_id = -1
        self.max_region_id = -1
        self.max_country_id = -1
        self.max_customer_id = -1

        self.first_names_male = self.load_file("data/first_names_male.txt")
        self.first_names_female = self.load_file("data/first_names_female.txt")
        self.last_names_male = self.load_file("data/last_names_male.txt")
        self.last_names_female = self.load_file("data/last_names_female.txt")
        self.mail_service_domains = self.load_file("data/mail_service_domains.txt")
        self.phone_prefixes = self.load_file("data/phone_prefixes.txt")

    def load_file(self, path: str) -> List[str]:
        path = path.replace('/', sep)
        with open(path, 'r', encoding="utf-8") as f:
            return f.read().splitlines()

    def get_random_sex(self) -> str:
        return choice(('m', 'f'))

    def get_random_first_name(self, sex='m') -> str:
        if sex == 'm':
            return choice(self.first_names_male)
        else:
            return choice(self.first_names_female)

    def get_random_last_name(self, sex='m') -> str:
        if sex == 'm':
            return choice(self.last_names_male)
        else:
            return choice(self.last_names_female)

    # def make_email(self, first_name: str, last_name: str) -> str:
    #     return f"{lower(first_name)}-{lower(last_name)@{choice(self.mail_service_domains)}}"

    def get_random_email(self) -> str:
        length = randint(6, 25)
        return ''.join(choice(ascii_lowercase) for _ in range(length)) + \
               '@' + choice(self.mail_service_domains)

    def get_random_numeral_str(self, length: int) -> str:
        return str(randint(10**(length-1), 10**length-1))

    def get_random_phone_nr(self) -> str:
        return choice(self.phone_prefixes) + \
               self.get_random_numeral_str(8)
