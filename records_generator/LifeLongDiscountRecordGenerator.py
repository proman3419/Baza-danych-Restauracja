from RecordGenerator import RecordGenerator


class LifeLongDiscountRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddLifeLongDiscount"
        self.discount_id = -1

    def generate_record(self) -> str:
        self.discount_id += 1
        if self.discount_id < self.helper.max_discount_id:
            args = [self.discount_id, self.helper.get_random_date_str()]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty LifeLongDiscount record"
