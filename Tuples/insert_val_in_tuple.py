'''WAP to take value from user in tuple'''
tpl=()
x=int(input("Enter the size of the tuple: "))
for i in range(x):
    y=int(input("Enter the elements"))
    tpl+=y,                             #where ',' is very important to define the tuple (in packing also)
print(tpl)    