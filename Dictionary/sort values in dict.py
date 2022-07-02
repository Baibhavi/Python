'''Sort values in dictionary in ascending order'''
d={}
val=[]
n=int(input("Enter number of keys: "))
for i in range(n):
    k=int(input("Enter key: "))
    v=int(input("Enter value: "))
    val.append(v)
    d.update({k:v})  
val.sort()
print(d)
print(val)