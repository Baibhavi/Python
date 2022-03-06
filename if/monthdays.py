#Write a program to input month number and print number of days in that month. 

x=int(input("Enter the month number\n"))
if(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
  print("There are 31 days in the given month.")
elif(x==2):
  print("There are 28 days in the given month and 29 days in leap year.")
else:
  print("There are 30 days in the given month.")
