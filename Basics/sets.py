my_set = {"January", "February", "March"}
# Printing sets are in random order unlike lists
print(my_set)
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)

# Lists are always in order and removing will remove the first occurrence
my_list = ["January", "February", "March", "January"]
my_list.remove("January")
print(my_list)