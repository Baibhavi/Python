'''Take a tuple make tuple from itself (nested tuple).'''

x=int(input("Enter the number of elements: "))
tpl1=()
for i in range(x):
    y=int(input("Enter the elements: "))
    tpl1+=y,
print(tpl1)    
tpl2=()
for i in range(x):
    tpl3=()
    tpl3+=tpl1[i],
    tpl2+=tpl3,
print(tpl2)        