'''Enter dictionary from user and sum the values.'''

d={}
sum=0
n=int(input("Enter the number of keys: "))
for i in range(n):
    k=int(input("Enter key: "))
    v=int(input("Enter value: "))
    sum+=v
    d.update({k:v})
print(d)
print("Sum of values: ",sum)