class MyBaseClass(object):
    string_a = None
    string_b = None

    def __init__(self, a, b):
        self.string_a = a
        self.string_b = b


class MyClass(object):
    my_strings: list[MyBaseClass] = None

    def __init__(self):
        self.my_strings = []


my_class = MyClass()

my_class.my_strings.append(MyBaseClass("hello", "world"))

print(my_class.my_strings[0].string_a)
print(my_class.my_strings[0].string_b)