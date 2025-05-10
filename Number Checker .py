number = int(input("Write your Number : "))

def check(number):
	checku = number % 2
	if checku == 0:
		print('Your number is even')
	else:
		print("Your number is odd")

result = check(number)