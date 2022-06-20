'''Remove all Characters in a String except alphabet'''
a=input("Enter string")
b=""
c='abcdefghijklmnopqrstuvwxyz'
a=a.lower()
for i in a:
    if (i in c):
        b=b+i
print(b)        