'''Find the sum of first and the last element of the list'''
n=int(input("Enter the length of the list"))
lst=[]
for i in range (n):
    lst.append(int(input("Enter the elements")))
print(lst)
print(lst[0]+lst[n-1])
