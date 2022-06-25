'''Sum up the elements of the list'''
lst=[]
n=int(input("Enter the length of the list: "))
for i in range(n):
    lst.append(int(input(f"Enter the element {i} of the list")))
print(lst)
print("The sum of the elements of the list is: ",sum(lst))    