from CountryRecordGenerator import CountryRecordGenerator
from RegionRecordGenerator import RegionRecordGenerator
from CityRecordGenerator import CityRecordGenerator


country_record_generator = CountryRecordGenerator()
region_record_generator = RegionRecordGenerator()
city_record_generator = CityRecordGenerator()

for i in range(10):
    print(country_record_generator.generate_record())
    print(region_record_generator.generate_record())
    print(city_record_generator.generate_record())
