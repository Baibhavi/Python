'''Write a program to find LCM and GCD of two numbers.'''
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
if x>y:
    x,y=y,x
for i in range (1,x+1) :
    if (x%i==0 and y%i==0) :
        gcd=i
print("GCD=",gcd) 
lcm=(x*y)//gcd
print("LCM",lcm)