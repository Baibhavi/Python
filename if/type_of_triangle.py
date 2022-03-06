#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle
x=float(input("Enter length of first side.\n"))
y=float(input("Enter length of second side.\n"))
z=float(input("Enter length of third side.\n"))
if(x+y>z and x+z>y and y+z>x):
  if(x==y==z):
    print("Equilateral")
  elif(x==y or y==z or x==z):
    print("isosceles")
  else:
    print("Scalene")
else:
  print("The triangle is invalid")
    
