'''list1=[(1,2),(3,4),(5,6)] ; list2=[(7,8),(9,10),(11,12)]
final list = [(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)] no. of rows and columns of both list
should be same -----> list interseption'''
lst1=[(1,2),(3,4),(5,6)]
lst2=[(7,8),(9,10),(11,12)]
lst=[]
for i in range(3):
    tpl=()                     # to define the type
    for j in range(2):
        tpl+=lst1[i][j],lst2[i][j]
        lst.append(tpl)
        tpl=()                # to empty the tuple
print(lst)        
