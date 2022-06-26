'''Print list = [(1,2),(3,4),(5,6)] entered from user '''
lst=[]
x=int(input("Enter the number of rows(tuples): "))
y=int(input("Enter the number of columns (elements in each tuple): "))
for i in range(x):
    tpl=()
    for j in range(y):
        n=int(input("Enter the element: "))
        tpl+=n,
    lst.append(tpl)
print(lst)        