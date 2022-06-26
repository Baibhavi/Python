'''Enter a tuple of string type from user and join all elements to convert into string'''
tpl=()
n=int(input("Enter the number of elements"))
for i in range(n):
    x=input("Enter the element: ")
    tpl+=x,
print(tpl)
k=''.join(tpl)
print(k)    