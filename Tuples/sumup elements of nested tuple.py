'''Sum of all the elements of nested tuple .'''
x=int(input("Enter the size of the tuple: "))
tpl1=()
for i in range(x):
    y=int(input("Enter element: "))
    tpl1+=y,
print("Tuple 1= ",tpl1)
tpl2=()
sum1=0
for i in range(x):
    tpl3=()
    tpl3+=tpl1[i],
    tpl2+=tpl3,   
    sum1+=tpl1[i]   #without using function
print("Tuple 2 = ",tpl2)
print("The sum of the elements of tuple 2 = ",sum1)
#using function
sum2=sum(tpl2)
print(sum2)
