# Initialising the List
myNumbers=[15,19,26,32,5,7,8]
print("List of numbers:")
print("[",end="")
for x in myNumbers:
	print(x,end=",")
print("]")
print("List of numbers that are greater than 12")
print("[",end="")
for x in myNumbers:
	#checking whether the number is greater than 12 or not
	if x>12:
		print(x,end=",")
print("]")