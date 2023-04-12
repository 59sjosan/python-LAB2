l=0
num=int(input("Enter the number of years: "))
# To check the rainfall for num of years
while(l<num):
  j=0
  k=0
  total=0
  while(j<12):
    print("Enter the rainfall amount for the month ",j+1,": ")
    k=int(input())
    #Adding all rainfall amount Value
    total=total+k
    j+=1
    l=l+1
  print("total:", total, "inches")
  #Calculating average rainfall by dividing it by 12
  print("Average monthly rainfall", total/12.0, "inches")