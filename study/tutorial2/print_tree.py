#!/usr/bin/python3
'''
decrement spaces by 1 each time through the loop
increament the hashes by 2 each time through the loop
save spaces to the stamp by calculating tree height - 1
decrement from tree hight untill it equals 0
print spaces and the hasshes for each row
print stump spaces and then 1 hash
'''
# get the number of raws for the tree
# convert into an integer
tree_height = eval(input("how tall is the tree: "))
# get the starting space for the top of the tree
spaces = tree_height - 1
# there is one hash to start tha will be incremented
hashes = 1
# save stump spaces till later
stump_spaces = tree_height - 1
# make sure the right number of rows are printed
while tree_height != 0:
    # print the spaces
    for i in range(spaces):
        print(' ', end="")
    # print the hashes
    for i in range(hashes):
        print('#', end="")
    # newline after each row is printed
    print()
    # the spaces are deremented by one each time
    spaces -= 1
    # the hashes are incremented by two each time
    hashes += 2
    # decrement tree height each time to jump out of the loop
    tree_height -= 1
# print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")