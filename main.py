import unittest


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello():
        return 'Hello world'


class Admin(User):
    def __init__(self, name, age):
        super().__init__(name, age)

    def mend_something():
        return 1101101


class Developer(Admin):
    def __init__(self, name, age):
        super().__init__(name, age)

    def write_code():
        return [0, 1, 0, 0, 1, 0]


class TestUsers(unittest.TestCase):

    def test_string(self):
        self.assertEqual(type(User.say_hello()), str)

    def test_integer(self):
        self.assertEqual(type(Admin.mend_something()), int)

    def test_list(self):
        self.assertEqual(type(Developer.write_code()), list)

    def test_numbers(self):
        for i in Developer.write_code():
            self.assertEqual(type(Developer.write_code()[i]), int)


if __name__ == '__main__':
    unittest.main()
