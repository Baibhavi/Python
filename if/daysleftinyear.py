print("Number of days left in 2019 :")
x=int(input("Enter the day"))
y=int(input("Enter the month"))
if y==1:
  a=31-x    
  b=31*6+28+30*4
elif y == 2 :
  a=28-x
  b=31*6+30*4
elif y==3:
  a=31-x    
  b=31*5+30*4
elif y==4:
  a=30-x    
  b=31*5+30*3
elif y==5:
  a=31-x    
  b=31*4+30*3
elif y==6:
  a=30-x    
  b=31*4+30*2
elif y==7:
  a=31-x    
  b=31*3+30*2
elif y==8:
  a=31-x
  b=31*2+30*2
elif y==9:
  a=30-x
  b=31*2+30
elif y==10:
  a=31-x
  b=31+30
elif y==11:
  a=30-x
  b=31
elif y==12:
  a=31-x
  b=0
else:
  print("Wrong input")
c=a+b  
  

print(f" {a} days and {y} months")
print(f" No of days left : {c}")
