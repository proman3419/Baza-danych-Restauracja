from random import choice, randint
from string import ascii_lowercase


class RecordGeneratorHelper:
    max_city_id = -1
    max_region_id = -1
    max_country_id = -1
    max_customer_id = -1

    first_names_male = ["Jan", "Jarosław", "Grzegorz", "Bartłomiej", "Dariusz"]
    first_names_female = ["Janina", "Anna", "Katarzyna", "Marzena", "Marta"]
    last_names_male = ["Kowalski", "Nowak", "Chrobak", "Woźniak", "Lewandowski"]
    last_names_female = ["Kowalska", "Nowak", "Chrobak", "Woźniak", "Lewandowska"]
    mail_service_domains = ["gmail.com", "op.pl", "yahoo.com", "wp.pl"]
    phone_prefixes = ["48", "81", "33", "44"]

    @staticmethod
    def get_random_sex() -> str:
        return choice(('m', 'f'))

    @staticmethod
    def get_random_first_name(sex='m') -> str:
        if sex == 'm':
            return choice(RecordGeneratorHelper.first_names_male)
        else:
            return choice(RecordGeneratorHelper.first_names_female)

    @staticmethod
    def get_random_last_name(sex='m') -> str:
        if sex == 'm':
            return choice(RecordGeneratorHelper.last_names_male)
        else:
            return choice(RecordGeneratorHelper.last_names_female)

    # @staticmethod
    # def make_email(first_name: str, last_name: str) -> str:
    #     return f"{lower(first_name)}-{lower(last_name)@{choice(RecordGeneratorHelper.mail_service_domains)}}"

    @staticmethod
    def get_random_email() -> str:
        length = randint(6, 25)
        return "".join(choice(ascii_lowercase) for _ in range(length)) + \
               "@" + choice(RecordGeneratorHelper.mail_service_domains)

    @staticmethod
    def get_random_numeral_str(length: int) -> str:
        return str(randint(10**(length-1), 10**length-1))

    @staticmethod
    def get_random_phone_nr() -> str:
        return choice(RecordGeneratorHelper.phone_prefixes) + \
               RecordGeneratorHelper.get_random_numeral_str(8)
