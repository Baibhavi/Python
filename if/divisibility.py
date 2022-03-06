x=int(input("Enter the number to be checked"))
if(x%5==0 and x%11==0):
  print("The given number is divisible by both 5 and 11")
elif(x%5==0 and x%11!=0):
  print("The number is only divisible by 5")
elif(x%11==0 and x%5!=0):
  print("The number is only divisible by 11")
else :
  print("The number is neither divisible by 5 nor by 11")
