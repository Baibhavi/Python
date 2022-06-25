'''WAP to count the frequency of given element of the list'''
n=int(input("Enter the length of the list"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter the elements")))
print(lst)
c=int(input("Enter the element you want to find the frequency of: "))
print(lst.count(c))    