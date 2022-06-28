'''Wap to insert a key and value from user'''
d={1:7}
print(d)
k=int(input("Enter key to be added: "))
v=int(input("Enter values to be added: "))
d.update({k:v})
print(d)
