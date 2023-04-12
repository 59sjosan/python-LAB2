a=[]

num=int(input("My numbers: "))
for x in range(1,num+1):
  a.append(x)

print(a)
b=[]
greater=int(input("list of numbers that are greater than: "))
for x in range(1,num+1):
  a.append(x)
  if(a[x-1]>greater):
    b.append(a[x-1])
else:
    pass
print(b)