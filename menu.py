from datetime import datetime as time
from khayyam import JalaliDatetime
from uuid import uuid4


# TODO-1: Add Item class here
# TODO-1: Add .sample() classmethod for Item which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)


class Item:
    _id = 0
    food_list = list()
    beverage_list = list()
    starter_list = list()
    item_list = list()

    def __init__(self, name, item_type, price):
        self.uuid = uuid4()
        self.item_id = self.generate_id()
        self.name = name
        self.item_type = item_type
        self.price = price
        self.datetime = time.now()
        self.item_list.append(self)

    @classmethod
    def sample(cls):
        return cls(
            name='potato',
            item_type='f',
            price=10000,
        )

    @property
    def jalali_datetime(self):
        return JalaliDatetime(self.datetime).strftime('%C')

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id


# TODO-2: Add item_id to the Item class, item_id should be auto incremental
# TODO-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# TODO-2: Change datetime attr to be assigned automatically in Item class
# TODO-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
