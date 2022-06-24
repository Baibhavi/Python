'''pattern
**************
******  ******
*****    *****
****      **** 
***        ***
**          **
*            *  '''
n=int(input("Enter the number of rows: "))
sp=0
for i in range(n,0,-1):
    print("*"*i + " "*sp + "*"*i, end=" ")
    print()
    sp+=2
