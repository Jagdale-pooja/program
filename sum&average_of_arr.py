n=int(input("enter the number of elements to be inserted:"))
a=[]

for i in range(0,n):
    elem=int(input("enter element:"))
    a.append(elem)
    avg=sum(a)/n
print("the sum is:",sum(a))
print("the avg is:",avg)
    
