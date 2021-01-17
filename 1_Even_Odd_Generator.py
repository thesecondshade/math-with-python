'''
	Even-Odd Vending Machine
'''
import sys


def isinteger():
	i = input('Please enter an integer:  ')
	i = int(i)
	print(i)
	for x in range(1,10):
		print(i+(x*2))

if __name__ == '__main__':
	try:
	    isinteger()
	except:
	    print('You did not enter an integer! Abort!')
	    sys.exit(1)  # abort

		
