'''Program to find whether an entered number is prime or not.'''

x=int(input("Enter the number to be checked "))
if x>1:
    for i in range (2,x-1):
        if x%i == 0:
            print(x,"is not prime")
        else : 
            print(x,"is prime")
else:
    print(x,"is not prime")
