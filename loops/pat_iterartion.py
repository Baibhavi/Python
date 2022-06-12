'''Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*   '''
n=int(input("Enter the number of rows"))
i = 1
while i <= n :
    print("*"*i,end=" ")
    print() 
    i += 1
i=n-1
while i>=1:
    print("*"*i, end=" ")
    print()
    i-=1    

#using nested loop
n=int(input("Enter the number of rows"))
for i in range (n):
    for j in range (i):
        print("*", end=" ")
    print()    
for i in range (n,0,-1) :
    for j in range(i):
        print("*", end =" ")
    print()        