'''WAP to insert multiple keys and values'''
d={}
n=int(input("Enter the number of keys: "))
for i in range(n):
    k=int(input("Enter the keys: "))
    v=int(input("Enter the values: "))
    d.update({k:v})
print(d)    