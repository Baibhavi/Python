'''Delete All Repeated Words in String'''
a=input("Write something")
b=a.split()
c=[]
for i in b:
    if (i not in c) :
        c.append(i)
k=' '.join(c)        
print(k)

    


