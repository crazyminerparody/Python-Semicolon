driving_distance = float(input('Enter the driving distance: '))
miles_per_gallon = float(input('Enter miles per gallon: '))
price_per_gallon = float(input('Enter price per gallon: '))

price = driving_distance * price_per_gallon/ miles_per_gallon
print ('Cost of driving is $' +str(price))
