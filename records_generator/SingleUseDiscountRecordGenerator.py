from RecordGenerator import RecordGenerator
from random import choice


class SingleUseDiscountRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddSingleUseDiscount"
        self.discount_id = -1

    def generate_record(self) -> str:
        self.discount_id += 1
        if self.discount_id < self.helper.max_order_id:
            args = [self.discount_id, self.helper.get_random_date_str(), self.helper.get_random_date_str(),
                    choice(['TRUE', 'FALSE'])]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty Single Use Discount record"
