from RecordGenerator import RecordGenerator


class ClientRecordGenerator(RecordGenerator):
    def __init__(self, helper):
        self.helper = helper
        self.procedure_name = "AddClient"
        self.last_customer_id = -1

    def generate_record(self) -> str:
        if self.last_customer_id < self.helper.max_customer_id:
            self.last_customer_id += 1
            sex = self.helper.get_random_sex()
            args = [self.last_customer_id, self.helper.get_random_first_name(sex), 
                    self.helper.get_random_last_name(sex)]
            return self.make_query(self.procedure_name, args)
        else:
            return "--Empty Client record"
