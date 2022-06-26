'''Create a tuple in the list. Last element of each tuple is to be replaced by a number '''
lst=[(1,2,3),(4,5,6),(7,8,9)]
lst2=[]
for i in lst:
    x=i[:-1]+(100,)
    lst2.append(x)
print(lst2)    