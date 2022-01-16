from CountryRecordGenerator import CountryRecordGenerator
from RegionRecordGenerator import RegionRecordGenerator
from CityRecordGenerator import CityRecordGenerator
from CustomerRecordGenerator import CustomerRecordGenerator
from ClientRecordGenerator import ClientRecordGenerator


country_record_generator = CountryRecordGenerator()
region_record_generator = RegionRecordGenerator()
city_record_generator = CityRecordGenerator()

customer_record_generator = CustomerRecordGenerator()
client_record_generator = ClientRecordGenerator()

for i in range(10):
    print(country_record_generator.generate_record())
    print(region_record_generator.generate_record())
    print(city_record_generator.generate_record())

    print(customer_record_generator.generate_record())
    print(client_record_generator.generate_record())
