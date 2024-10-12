my_list = [42, "hello", 3.14, True, None, [1, 2, 3], (4, 5), {"key": "value"}, {1, 2, 3}, b"bytes"]


my_list[0] = 100          
my_list[1] = "world"      
my_list[2] = 2.71        
my_list[3] = False       
my_list[4] = "new_value"  

print(my_list)
#2
number_list = [1, 2, 3, 4, 5]

sum_of_elements = sum(number_list)

print(sum_of_elements)
#3

number_list = [1, 2, 3, 4, 5]


doubled_list = [x * 2 for x in number_list]


print(doubled_list)