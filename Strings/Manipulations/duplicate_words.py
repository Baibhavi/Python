'''. Print all the duplicates in the input string.'''
a=input("Write something")
a=a.lower()
a=a.split()
b=[]
for i in a:
    c=a.count(i)
    if c>1:
        if i not in b:
            b.append(i)
b=' '.join(b)     
print(b)   