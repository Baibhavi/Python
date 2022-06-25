'''WAP to delete element of the list'''
#To delete the last element of the list
lst=[1,2,3,4,5,6,7,8,9,10]
lst.pop()
print(lst)

#To delete the elements using index number
lst.pop(3)
print(lst)

#To delete the element using the name of the element
lst.remove(2)
print(lst)