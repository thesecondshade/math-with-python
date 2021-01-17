'''
	Unit Converter
'''

def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')
	print('3. Farenheit to Celsius')
	print('4. Celsius to Farenheit')

def km_miles():
	km = float(input('Enter distance in kilometers: '))
	miles = km / 1.609
	print('Distance in miles: {0}'.format(miles))

def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609
	print('Distance in kilometers: {0}'.format(km))

def f_c():
	farenheit = float(input('Enter temperature in Farenheit: '))
	celsius = (farenheit - 32) * (5 / 9)
	print('Temperature in Celsius: {0}'.format(celsius))

def c_f():
	celsius = float(input('Enter temperature in Celsius: '))
	farenheit = (celsius / (5 / 9))+ 32
	print('Temperature in Farenheit: {0}'.format(farenheit))


if __name__ == '__main__':
	print_menu()
	choice = input('Which conversion would you like to do?:')
	if choice == '1':
		km_miles()
	if choice == '2':
		miles_km()
	if choice == '3':
		f_c()
	if choice == '4':
		c_f()
