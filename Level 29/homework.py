weight = float(input())  
height = float(input())  

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")
    number_list = [1, 2, 3, 4, 5]


product_of_elements = 1
for num in number_list:
    product_of_elements *= num


print(product_of_elements)