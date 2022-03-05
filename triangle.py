a=int(input("Enter the length of the first side of the triangle"))
b=int(input("Enter the length of the second side of the triangle"))
c=int(input("Enter the length of the third side of the triangle"))
if(a+b>c and a+c>b and b+c>a):
  if(a=b=c):
    print("Equilateral Triangle")
  elif(a=b or b=c or a=c):
    print("Isosceles Triangle")
  else :
    print("Scalene Triangle")
else :
  print("The Triangle is invalid")
    
  
