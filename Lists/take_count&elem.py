'''Take and count elements from the user'''
x=int(input("Enter the length of the list"))
lst=[]
for i in range(x):
    lst.append(input("Enter the element"))
    #lst.insert(i,input())
print(lst)  
