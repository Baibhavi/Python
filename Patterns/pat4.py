'''Pattern4
  * * * * *
    * * * *
      * * *
        * *
          * '''

n=int(input("Enter the number of rows:"))
i=n
while i!=0:
    print(" "*(n-i) + "*"*i)  
    i-=1        
