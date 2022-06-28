'''WAP to access the value of a key without deleting it .'''

d={1:2,3:4,5:6}
print(d)
x=int(input("Enter the key whose value you want: "))
v=d.get(x)
print("Value of ",x," is ",v)