'''Adding elements in the existing list'''
#Inserting elements from back/last/end
lst1=[1,2,3,4]
lst1.append(int(input("Enter the element to be inserted: ")))
print(lst1)

#Inserting element at any index
lst1.insert(int(input("Enter the index where element is to be inserted:")),int(input("Enter the element")))
print(lst1)

#Inserting more than one element from end
n=int(input("Enter the number of elements to be inserted: "))
lst2=[]
for i in range(n):
    lst2.append(int(input("Enter the elements: ")))
lst1.extend(lst2)  
print(lst1)