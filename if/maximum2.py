x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=int(input("Enter the third number"))
if (x>y):
  if(x>z):
    print(f'{x} is greatest')
  else:
    print(f'{z} is greatest')
elif(x<y):
  if(y>z):
    print(f'{y} is greatest')
  else:
    print(f'{z} is greatest')
else :
  print("All three are equal")
