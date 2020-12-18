from datetime import datetime as time
from uuid import uuid4
from khayyam import JalaliDatetime


# TODO-1: Add Bill class here
# TODO-1: Add Payment class here
# TODO-1: Add .sample() classmethod for Bill and Payment which returns

# an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)


class Bill:
    bill_list = list()

    def __init__(self, total_price, payment):
        self.uuid = uuid4()
        self.total_price = total_price
        self.payment = payment

    @classmethod
    def sample(cls):
        return cls(
            total_price=12000,
            payment=Payment.sample()
        )


class Payment:
    payment_list = list()

    def __init__(self, payment_type, is_paid, price):
        self.uuid = uuid4()
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.datetime = time.now()
        self.jalali_datetime = JalaliDatetime.now().strftime('%C')
        self.price = price

    @classmethod
    def sample(cls):
        return cls(
            payment_type='a',
            is_paid=True,
            price=12000
        )

# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
#       to get from input
# TODO-2: Change datetime attr to be assigned automatically in Payment class
# TODO-2: Add jalali_datetime property to the Payment class


# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments
