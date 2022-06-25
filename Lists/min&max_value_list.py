'''Find minimum and maximum value of the elements of the list'''
n=int(input("Enter the length of the list: "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter the elements of the list: ")))
print(lst)
print("The maximum value of the elements of the list",max(lst)) 
print("The minimum value of the elements of the list",min(lst))   