#colect input from user
#calculate the number of boxes of pizza the user will buy(assuming each guest eats 1 slice)
#how many slices will be left over 
#total amount the customer has to pay
import math

pizza_sample = """
piza Type     Number of slices      Price per box
Sapa Size        4                    2000
Small Size       6                    2400
Big Boys         8                    3000
Odogwu           12                   4200
"""
print(pizza_sample)

order = input("What are ur orders:").lower()
if order == "sapa size":
    slices = 4
    price_per_box = 2000
elif order == "small size":
    slices = 6
    price_per_box = 2400
elif order == "big boys":
    slices = 8
    price_per_box = 3000
elif order == "odogwu":
    slices = 12
    price_per_box = 4200
else:
    print("invalid input")
    exit()

number_of_guests = int(input("Enter the number of guests: "))
  
number_of_box = math.ceil(number_of_guests / slices) 
remains = (slices - number_of_guests)
price = number_of_box * price_per_box
 
 

print("==============This is your order summary===============")
print(f"Number of guests: {number_of_guests}")
print(f"Pizza boxes needed: {number_of_box} box")
print(f"Leftover pizza slices: {remains}")
print(f"The total pizza cost is: ${price}")
print("========================================================")













