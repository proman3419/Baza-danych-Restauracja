from Helper import Helper
from CountryRecordGenerator import CountryRecordGenerator
from RegionRecordGenerator import RegionRecordGenerator
from CityRecordGenerator import CityRecordGenerator
from CustomerRecordGenerator import CustomerRecordGenerator
from ClientRecordGenerator import ClientRecordGenerator
from CompanyRecordGenerator import CompanyRecordGenerator
from TableRecordGenerator import TableRecordGenerator
from ReservationRecordGenerator import ReservationRecordGenerator
from RestaurantEmployeeGenerator import RestaurantEmployeeGenerator
from TableHistRecordGenerator import TableHistRecordGenerator
from IndividualReservationRecordGenerator import IndividualReservationRecordGenerator
from OrderRecordGenerator import OrderRecordGenerator
from DiscountRecordGenerator import DiscountRecordGenerator
from IndividualReservationDetailsRecordGenerator import IndividualReservationDetailsRecordGenerator
from CompanyReservationRecordGenerator import CompanyReservationRecordGenerator
from CompanyReservationDetailsRecordGenerator import CompanyReservationDetailsRecordGenerator
from CompanyEmployeeReservationDetailsRecordGenerator import CompanyEmployeeReservationDetailsRecordGenerator

helper = Helper()

country_record_generator = CountryRecordGenerator(helper)
region_record_generator = RegionRecordGenerator(helper)
city_record_generator = CityRecordGenerator(helper)

customer_record_generator = CustomerRecordGenerator(helper)
client_record_generator = ClientRecordGenerator(helper)
company_record_generator = CompanyRecordGenerator(helper)

table_record_generator = TableRecordGenerator(helper)
restaurant_employee_generator = RestaurantEmployeeGenerator(helper)
reservation_record_generator = ReservationRecordGenerator(helper)
table_hist_record_generator = TableHistRecordGenerator(helper)
individual_reservation_record_generator = IndividualReservationRecordGenerator(helper)
order_record_generator = OrderRecordGenerator(helper)
discount_record_generator = DiscountRecordGenerator(helper)
individual_reservation_details_record_generator = IndividualReservationDetailsRecordGenerator(helper)
company_reservation_record_generator = CompanyReservationRecordGenerator(helper)
company_reservation_details_record_generator = CompanyReservationDetailsRecordGenerator(helper)
company_employee_reservation_details_record_generator = CompanyEmployeeReservationDetailsRecordGenerator(helper)

for i in range(1):
    print(country_record_generator.generate_record())
    print(region_record_generator.generate_record())
    print(city_record_generator.generate_record())

    print(customer_record_generator.generate_record())
    print(client_record_generator.generate_record())
    print(company_record_generator.generate_record())

    print(table_record_generator.generate_record())
    print(restaurant_employee_generator.generate_record())
    print(reservation_record_generator.generate_record())
    print(table_hist_record_generator.generate_record())
    print(discount_record_generator.generate_record())
    print(order_record_generator.generate_record())

    print(individual_reservation_record_generator.generate_record())
    print(individual_reservation_details_record_generator.generate_record())
    print(company_reservation_record_generator.generate_record())
    print(company_reservation_details_record_generator.generate_record())
    print(company_employee_reservation_details_record_generator.generate_record())
