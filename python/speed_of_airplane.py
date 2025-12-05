take_off_speed = float(input('Enter your speed: '))
airplane_acceleration = float(input('Enter the acceleration of the airplane: '))

length = take_off_speed ** 2 / 2 * airplane_acceleration

print('The minimum runaway for this airplane is: ', round(length, 2))
