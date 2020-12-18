from uuid import uuid4


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

    def __init__(self, capacity, number, reserved, is_available):
        self.uuid = uuid4()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available
        self.table_list.append(self)

    @classmethod
    def sample(cls):
        return cls(
            capacity=5,
            number=1,
            reserved=False,
            is_available=True
        )
