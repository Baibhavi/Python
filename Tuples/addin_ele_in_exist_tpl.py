'''WAP to add elements in an existing tuple'''
tpl=(1,2,)
n=int(input("Enter the number of elements you want to add: "))
for i in range(n):
    y=int(input("Enter elements: "))
    tpl+=y,
print(tpl)    