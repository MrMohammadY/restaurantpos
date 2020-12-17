from datetime import datetime as time
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
    food_list = list()
    beverage_list = list()
    starter_list = list()

    def __init__(self, uuid, name, item_type, price, datetime):
        self.uuid = uuid
        self.name = name
        self.item_type = item_type
        self.price = price
        self.datetime = datetime

    @classmethod
    def sample(cls):
        return cls(uuid=1, name='potato', item_type='f', price='1000', datetime=time.now())

# TODO-2: Add item_id to the Item class, item_id should be auto incremental
# TODO-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# TODO-2: Change datetime attr to be assigned automatically in Item class
# TODO-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
