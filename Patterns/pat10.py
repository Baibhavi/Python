'''Pattern 10
*************
*           *
*           *
*           *
*************  '''
r=int(input("Enter the rows: "))
for i in range(r):
    for j in range(r):
        if i==0 or i==r-1 or j==0 or j==r-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()           
