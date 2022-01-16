from Helper import Helper
from CountryRecordGenerator import CountryRecordGenerator
from RegionRecordGenerator import RegionRecordGenerator
from CityRecordGenerator import CityRecordGenerator
from CustomerRecordGenerator import CustomerRecordGenerator
from ClientRecordGenerator import ClientRecordGenerator
from CompanyRecordGenerator import CompanyRecordGenerator


helper = Helper()

country_record_generator = CountryRecordGenerator(helper)
region_record_generator = RegionRecordGenerator(helper)
city_record_generator = CityRecordGenerator(helper)

customer_record_generator = CustomerRecordGenerator(helper)
client_record_generator = ClientRecordGenerator(helper)
company_record_generator = CompanyRecordGenerator(helper)

for i in range(10):
    print(country_record_generator.generate_record())
    print(region_record_generator.generate_record())
    print(city_record_generator.generate_record())

    print(customer_record_generator.generate_record())
    print(client_record_generator.generate_record())
    print(company_record_generator.generate_record())
