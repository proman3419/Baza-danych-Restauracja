from CityRecordGenerator import CityRecordGenerator
from ClientRecordGenerator import ClientRecordGenerator
from CompanyEmployeeReservationDetailsRecordGenerator import CompanyEmployeeReservationDetailsRecordGenerator
from CompanyRecordGenerator import CompanyRecordGenerator
from CompanyEmployeeReservationDetailsRecordGenerator import CompanyEmployeeReservationDetailsRecordGenerator
from CompanyReservationDetailsRecordGenerator import CompanyReservationDetailsRecordGenerator
from CompanyReservationRecordGenerator import CompanyReservationRecordGenerator
from CountryRecordGenerator import CountryRecordGenerator
from CustomerRecordGenerator import CustomerRecordGenerator
from DiscountRecordGenerator import DiscountRecordGenerator
from DishCategoryRecordGenerator import DishCategoryRecordGenerator
from DishRecordGenerator import DishRecordGenerator
from EmployeeRecordGenerator import EmployeeRecordGenerator
from Helper import Helper
from IndividualReservationDetailsRecordGenerator import IndividualReservationDetailsRecordGenerator
from IndividualReservationRecordGenerator import IndividualReservationRecordGenerator
from LifeLongDiscountHistRecordGenerator import LifeLongDiscountHistRecordGenerator
from LifeLongDiscountRecordGenerator import LifeLongDiscountRecordGenerator
from MenuItemRecordGenerator import MenuItemRecordGenerator
from OrderDetailsRecordGenerator import OrderDetailsRecordGenerator
from OrderRecordGenerator import OrderRecordGenerator
from RegionRecordGenerator import RegionRecordGenerator
from ReservationRecordGenerator import ReservationRecordGenerator
from RestaurantEmployeeGenerator import RestaurantEmployeeGenerator
from SingleUseDiscountHistRecordGenerator import SingleUseDiscountHistRecordGenerator
from SingleUseDiscountRecordGenerator import SingleUseDiscountRecordGenerator
from TableHistRecordGenerator import TableHistRecordGenerator
from TableRecordGenerator import TableRecordGenerator
from os import remove


helper = Helper()

cityRecordGenerator = CityRecordGenerator(helper)
clientRecordGenerator = ClientRecordGenerator(helper)
companyEmployeeReservationDetailsRecordGenerator = CompanyEmployeeReservationDetailsRecordGenerator(helper)
companyRecordGenerator = CompanyRecordGenerator(helper)
companyReservationDetailsRecordGenerator = CompanyReservationDetailsRecordGenerator(helper)
companyReservationRecordGenerator = CompanyReservationRecordGenerator(helper)
countryRecordGenerator = CountryRecordGenerator(helper)
customerRecordGenerator = CustomerRecordGenerator(helper)
discountRecordGenerator = DiscountRecordGenerator(helper)
dishCategoryRecordGenerator = DishCategoryRecordGenerator(helper)
dishRecordGenerator = DishRecordGenerator(helper)
employeeRecordGenerator = EmployeeRecordGenerator(helper)
individualReservationDetailsRecordGenerator = IndividualReservationDetailsRecordGenerator(helper)
individualReservationRecordGenerator = IndividualReservationRecordGenerator(helper)
lifeLongDiscountHistRecordGenerator = LifeLongDiscountHistRecordGenerator(helper)
lifeLongDiscountRecordGenerator = LifeLongDiscountRecordGenerator(helper)
menuItemRecordGenerator = MenuItemRecordGenerator(helper)
orderDetailsRecordGenerator = OrderDetailsRecordGenerator(helper)
orderRecordGenerator = OrderRecordGenerator(helper)
regionRecordGenerator = RegionRecordGenerator(helper)
reservationRecordGenerator = ReservationRecordGenerator(helper)
restaurantEmployeeGenerator = RestaurantEmployeeGenerator(helper)
singleUseDiscountHistRecordGenerator = SingleUseDiscountHistRecordGenerator(helper)
singleUseDiscountRecordGenerator = SingleUseDiscountRecordGenerator(helper)
tableHistRecordGenerator = TableHistRecordGenerator(helper)
tableRecordGenerator = TableRecordGenerator(helper)


if __name__ == "__main__":
    def loop(record_generator, records_cnt):
        for i in range(records_cnt):
            with open(output_file, "a+", encoding="utf-8") as f:
                f.write(record_generator.generate_record() + '\n')

    output_file = "populate_db.sql"
    records_cnt = 100

    try:
        remove(output_file)
    except OSError:
        pass

    loop(tableRecordGenerator, records_cnt)
    loop(customerRecordGenerator, records_cnt)

    loop(countryRecordGenerator, records_cnt)
    loop(regionRecordGenerator, records_cnt)
    loop(cityRecordGenerator, records_cnt)

    loop(clientRecordGenerator, records_cnt)
    loop(companyRecordGenerator, records_cnt)
    loop(employeeRecordGenerator, records_cnt)

    loop(discountRecordGenerator, records_cnt)
    loop(lifeLongDiscountRecordGenerator, records_cnt)
    loop(lifeLongDiscountHistRecordGenerator, records_cnt)
    loop(singleUseDiscountRecordGenerator, records_cnt)
    loop(singleUseDiscountHistRecordGenerator, records_cnt)

    loop(dishCategoryRecordGenerator, records_cnt)
    loop(dishRecordGenerator, records_cnt)
    loop(menuItemRecordGenerator, records_cnt)

    loop(restaurantEmployeeGenerator, records_cnt)
    loop(orderRecordGenerator, records_cnt)
    loop(orderDetailsRecordGenerator, records_cnt)

    loop(reservationRecordGenerator, records_cnt)
    loop(tableHistRecordGenerator, records_cnt)
    loop(individualReservationRecordGenerator, records_cnt)
    loop(individualReservationDetailsRecordGenerator, records_cnt)
    loop(companyReservationRecordGenerator, records_cnt)
    loop(companyReservationDetailsRecordGenerator, records_cnt)
    loop(companyEmployeeReservationDetailsRecordGenerator, records_cnt)
