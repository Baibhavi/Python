'''Find the index of given value/element of the list'''
n=int(input("Enter length of the list"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter the element: ")))
print(lst)    
k=int(input("Enter the value whose index is needed: "))
print(f"The index at value {k} is {lst.index(k)}")