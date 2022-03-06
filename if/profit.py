#Write a program to calculate profit or loss. 
ci=float(input("Enter the cost price"))
si=float(input("Enter the selling price"))
if(si>ci):
  print("Profit of ",si-ci)
elif(si<ci):
  print("Loss of ",ci-si)
else:
  print("No profit no loss")
