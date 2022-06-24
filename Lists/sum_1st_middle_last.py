'''Find the sum of first,middle and the last element of the list'''
n=int(input("Enter the length of the list"))
lst=[]
for i in range (n):
    lst.append(int(input("Enter the elements")))
print(lst)
if n%2==0:
    mid=((n//2) + ((n//2)+1))//2
    sum=lst[0]+lst[n-1]+lst[mid]
else:
    mid=n//2
    sum=lst[0] + lst[n-1] + lst[mid]
print(sum)      

