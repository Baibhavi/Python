'''Pattern 9
 *     *
 **    **
 ***   ***
 ****  ****
 ***** *****  '''
r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    print("*"*i + " "*r + "*"*i , end=" ")
    print()
    r-=1