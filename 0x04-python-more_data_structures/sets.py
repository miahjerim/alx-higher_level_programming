set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 # union()
intersection_set = set1 & set2 # intersection()
difference_set = set2 - set1 # difference()
symmetric_difference_set = set1 ^ set2 #symmetric_difference()
modified_set = set()

for element in union_set:
    if element % 2 == 0:
        print("{} is even".format(element))
    else:
        print("{} is odd".format(element))

for element in union_set:
    modified_set.add(element * 2)
print("{}".format(union_set))

print("{}".format(intersection_set))

print("{}".format(difference_set))

print("{}".format(symmetric_difference_set))

print("modified_set is: {}".format(modified_set))