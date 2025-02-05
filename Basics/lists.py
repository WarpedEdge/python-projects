my_list = ["January", "February", "March"]
print(my_list[2])
my_list.append("April")
print(my_list[4])

# Lists are always in order and removing will remove the first occurrence
my_list = ["January", "February", "March", "January"]
my_list.remove("January")
print(my_list)