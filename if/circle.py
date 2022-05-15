'''Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and 
determine whether the point is inside the circle, on the circle or outside the circle.'''

x1= int(input("Enter the centre point in x coordinate "))
y1=int(input("Enter the centre point in y coordinates "))
r= int(input("Enter the radius of the circle "))
x2 = int(input("Enter the x coordinate of the point to be checked "))
y2 = int(input("Enter the y coordinate of the point to be checked "))
p=(((x1-x2)**2)+((y1-y2)**2))**0.5
if r>p :
  print(f"The given point {x2,y2} lies inside the circle.")
elif r<p :  
  print(f"The given point {x2,y2} lies outside the circle.")
elif r==p :
  print(f"The given point {x2,y2} lies on the border of the circle.")
else:
  print("Wrong entry")
