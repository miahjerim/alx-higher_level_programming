#!/usr/bin/python3
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_dict["key3"] = "new value"
if "key1" in my_dict:
    print("{}".format("The key exists"))
else:
    print("{}".formart("Key does not exist"))

# getting all the keys
keys = my_dict.keys()
print("{}".format(keys))

# getting all values
values = my_dict.values()
print("{}".format(values))

# getting all key-value pairs as tuples
items = my_dict.items()
print("{}".format(items))


print("{}".format(my_dict["key2"]))
print("{}".format(my_dict))
print("{}".format(my_dict.get("key4", "default value")))
print("{}".format(len(my_dict)))