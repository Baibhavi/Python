#Write a program to input angles of a triangle and check whether triangle is valid or not. 
x=float(input("Enter the first angle of the triangle\n")) 
y=float(input("Enter the second angle of the triangle\n"))
z=float(input("Enter the third angle of the triangle\n"))
if(x+y+z==180):
  print("The triangle is valid.")
else:
  print("The traingle is invalid")
  
