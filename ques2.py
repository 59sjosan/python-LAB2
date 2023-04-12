#Taking input
a=int(input("Starting number of organisms: "))
per=int(input("Average daily percentage increase: "))
b=int(input("Enter the number of days to display the final data: "))
print("Day Approximate \t Population")
print("----------------------------------------------------")
for x in range(b):
	print(x+1,"\t\t\t",a)
	#Increasing value of population
	a=a+(per*a/100)
  