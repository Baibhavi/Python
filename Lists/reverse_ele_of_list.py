'''WAP to reverse the elements of the list'''
lst=[1,2,3,4,5,6,7,8]
l=[]
for i in lst:
    l.insert(0,i)
print(l)    

# Using function
lst.reverse()
print(lst)