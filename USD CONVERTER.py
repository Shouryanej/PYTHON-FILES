#USD TO INR CONVERTER 
USD = int(input('Write your value which have to be converted to INR : '))

def converter(USD):
	inr = USD * 85.31
	return inr
	
print(f"Your INR value is : ", converter(USD))