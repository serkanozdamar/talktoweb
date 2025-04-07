my_list = ["3.14", "150.5", "5", 1, 2]
"""
for i in range(len(my_list)):
    my_list[i] = float(my_list[i]) 
"""
my_list = [float(my_list[i]) for i in range(len(my_list))]