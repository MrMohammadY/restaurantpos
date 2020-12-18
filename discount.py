from datetime import datetime as time


# TODO-2: Add Discount class here
class Discount:
    discount_list = list()

    def __init__(self, code, count, start_date, end_date, percentage, minimum_order, maximum_order):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order

    @classmethod
    def sample(cls):
        return cls(
            code='15562',
            count=1,
            start_date=time.now(),
            end_date=time.now(),
            percentage=2,
            maximum_order=5,
            minimum_order=8
        )
