'''Print the Words Ending with Letter ‘s’
'''
a=input("Write something")
a=a.lower()
a=a.split()
b=input("Word ending with letter:")
lst=[]
for i in a:
    l=len(i)
    if i[l-1]==b: 
        lst.append(i)
k=' '.join(lst)            
print(k)        