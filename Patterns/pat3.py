'''Pattern3
        *
      * *
    * * *
  * * * *
* * * * *  '''
n=int(input("Enter the number of rows"))
i=1
while i!=n:
    print(" "*(n-i) + "*"*i)
    i+=1