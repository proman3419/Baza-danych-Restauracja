from RecordGenerator import RecordGenerator
from random import choice


class SingleUseDiscountRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddSingleUseDiscount"
        self.discount_id = -1

    def generate_record(self) -> str:
        if self.discount_id < self.helper.max_discount_id:
            self.discount_id += 1
            args = [self.discount_id, self.helper.get_random_date_str(), self.helper.get_random_date_str(),
                    choice(['TRUE', 'FALSE'])]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty SingleUseDiscount record"
