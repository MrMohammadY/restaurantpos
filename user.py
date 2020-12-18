# TODO-1: Add Supervisor class Here
# TODO-1: Add .sample() classmethod for Supervisor which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)


class Supervisor:
    user_list = list()

    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    @classmethod
    def sample(cls):
        return cls(
            username='Ali',
            password='1234',
            phone_number='09101916484'
        )
