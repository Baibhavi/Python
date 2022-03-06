#Write a program to find all roots of a quadratic equation.

a=float(input("Enter the coefficient of x sq"))
b=float(input("Enter the coefficient of x"))
c=float(input("Enter the constant term"))
D=(b**2)-(4*a*c)
if(D>0):
  print("Real and distinct root \n")
  print((-b+D)/2*a)
  print((-b-D)/2*a)
elif(D<0):
  print("Imaginary roots")
  print((-b+D)/2*a)
  print((-b-D)/2*a)
else:
  print("Real and same roots")
  print((-b+D)/2*a)
  print((-b-D)/2*a)
