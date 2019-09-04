#msg = 'Welcome to this program
#print(msg)

"""
x = int(input('Ente a number: '))
x += 20
print(x)
"""

"""
print(y)
"""

while True:
	try:
		x =  int(input('Enter a number: '))
		break
	except:
		print('That\'s not a valid number')	
	finally:
		print('\nAttempted input\n')	

