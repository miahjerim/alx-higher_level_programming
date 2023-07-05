#!/usr/bin/python3
my_dict = {"name": "John", "age": 25, "city": "kisumu"}
# using key()method
for key in my_dict.keys():
    print("{}".format(key))
print()
# directly iterating over the dictionary
for key in my_dict:
    print("{}".format(key))
print()
# iterating over values using values()method
for value in my_dict.values():
    print("{}".format(value))
print()
# iterrating over key-value pairs using items()
for key, value in my_dict.items():
    print("{} " "{} ".format(key, value))
