#Write a program to check whether a year is leap year or not. 
x=int(input("Enter the year to be checked\n"))
if (x%400==0 and x%100!=0 or x%4==0):
  print("Leap Year")
else:
  print("Not Leap Year")
