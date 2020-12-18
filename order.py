from menu import Item
from saloon import Table
from uuid import uuid4
from finance import Bill
from datetime import datetime as time
from khayyam import JalaliDatetime
from finance import Payment

a = Item.sample()
b = Item.sample()
t1 = Table.sample()
t2 = Table(capacity=5, number=5, reserved=False, is_available=True)


# TODO-1: Add Order model here
# TODO-1: Add .sample() classmethod for Order which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

class Order:
    order_list = list()
    order_list_unpaid = list()

    def __init__(self, item_dict, in_out, table):
        self.uuid = uuid4()
        self.item_dict = item_dict
        self.in_out = in_out
        self.datetime = time.now()
        self.table = self.assign_table()
        self.bill = self.set_bill()
        self.save_order(self)

    @classmethod
    def sample(cls):
        return cls(
            item_dict={a: 2, b: 2},
            in_out='I',
            table=Table.sample(),
        )

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime).strftime('%C')

    @classmethod
    def save_order(cls, self):
        cls.order_list.append(self)

    @classmethod
    def save_unpaid_order(cls, self):
        if self.bill.payment.is_paid is False:
            cls.order_list_unpaid.append(self)

    def calculate_total_price(self):
        total_price = 0
        for value in self.item_dict.items():
            total_price += value[0].price * value[1]
        return total_price

    @staticmethod
    def assign_table():
        for table in Table.table_list:
            if table.is_available:
                table.is_available = False
                return table

    def set_bill(self):
        return Bill(
            self.calculate_total_price(), Payment(payment_type='mel', price=self.calculate_total_price(), is_paid=False)
        )


o = Order.sample()
# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# TODO-2: Add jalali_datetime property to the Order class
# TODO-2: uuid and datetime attrs should be assigned automatically
# TODO-2: Store a list of orders and a list for un_paid_orders
# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
# TODO-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order class
