age = int(input('Enter your age: '))
maximum_heart_rate = 220 - age
lower_range = 50/100 * maximum_heart_rate
higher_range = 85/100 * maximum_heart_rate
print('Your maximum Heart Rate is: ', maximum_heart_rate)
print('Your target heart range is: ', lower_range, '-', higher_range)
