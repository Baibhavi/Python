#Write a program to input all sides of a triangle and check whether triangle is valid or not.
x=float(input("Enter the length of first side\n"))
y=float(input("Enter the length of second side\n"))
z=float(input("Enter the length of third side\n"))
if(x+y>z or x+z>y or y+z>x):
   print("The triangle is valid.")
else:
   print("The triangle is invalid")
