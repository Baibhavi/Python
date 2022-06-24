'''Find the sum of odd index and even index element of the list'''
n=int(input("Enter the length of the list"))
lst=[]
sum=0
sum2=0
for i in range (n):
    lst.append(int(input("Enter the elements")))
    if i%2==0:
        sum+=lst[i]
    else:
        sum2+=lst[i]
print(lst)
print("Sum of even index elements :",sum)
print("Sum of odd index elements :",sum2)        

