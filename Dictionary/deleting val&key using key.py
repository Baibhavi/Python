'''WAP to delete a value as well as key'''

# using key
d={1:2,3:4,4:5,6:9}
k=int(input("Enter the element/key to be deleted: "))
d.pop(k)
print(d)

# from last
d.popitem()
print(d)

#delete entire dictionary
d.clear()
print(d)