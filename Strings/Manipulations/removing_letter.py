'''Remove “b” and “ac” from a given string
'''
a=input("Write something")
b=""
c='bac'
for i in a:
    if i not in c:
        b+=i
print(b)        


    