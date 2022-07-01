'''Create a dictionary from user and find frequency of characters.'''
d={}
n=int(input("Enter the number of keys: "))
for i in range(n):
    k=int(input("Enter the key: "))
    v=int(input("Enter the value: "))
    d.update({k:v})
print(d)
d1={}
vals=list(d.values())
for j in vals:
    d1[j]=vals.count(j)
print(d1)
d2={}
key=list(d.keys())
for k in key:
    if k not in d2:
        d2[k]=0
    d2[k]+=1
print(d2)        

