# TODO-1: Add Table class here
# TODO-1: Add .sample() classmethod for Table which returns  an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

class Table:
    table_list = list()

    def __init__(self, uuid, capacity, number, reserved, is_available):
        self.uuid = uuid
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available

    @classmethod
    def sample(cls):
        return cls(uuid=1, capacity=5, number=1, reserved=False, is_available=True)


