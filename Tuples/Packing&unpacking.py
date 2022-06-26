#Packing of tuple
tpl=1,2,3,5
print(tpl)

#Unpacking of tuple
n1,n2,n3,n4=tpl
print(n1)
'''if number of variables are less than the no. of elements , it will throw error,
until we make one of the variable 'a list':'''
*n1,n2,n3=tpl
print(n1)
