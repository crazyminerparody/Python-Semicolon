first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

sum = first_num + second_num + third_num
average = sum/3
product = first_num * second_num * third_num

largest = first_num

if (second_num > largest):
    largest = second_num
if (third_num > largest):
    largest = third_num

smallest = first_num

if (second_num < smallest):
    smallest = second_num
if(third_num < smallest):
    smallest = third_num

print('The sum,average and product of the numbers are', sum, '-', average, 'and', product, "respectively")
print('The greatest and smallest numbers are: ', largest, 'and', smallest, "respectively")
