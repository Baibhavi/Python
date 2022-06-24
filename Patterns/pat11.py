'''Pattern 11
       *
     * * *
   * * * * *
  * * * * * * *
* * * * * * * * * 
 * * * * * * * * 
    * * * * *
      * * * 
        *      '''
r=int(input("Enter the number of rows: "))
for i in range(r):
    for j in range(r-i-1):
        print(" ", end=" ")
    for k in range(2*i + 1) :
        print("* ",end="")
    print() 
for i in range(r-1):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(2*(r-i-1)-1):
        print("* ",end="") 
    print()    
