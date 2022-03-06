'''Write a program to input basic salary of an employee and calculate its Gross salary according to 
	following: 
	Basic Salary <= 10000 : HRA = 20%, DA = 80% 
	Basic Salary <= 20000 : HRA = 25%, DA = 90% 
	Basic Salary > 20000 : HRA = 30%, DA = 95%''' 
x=int(input("Enter your basic salary"))
if(x<=10000):
  ta= x + 0.2*x + 0.8*x
  print("Your Total Salary is ",ta)
elif(x<=20000):
  ta = x + 0.25*x + 0.9*x
  print("Your Total Salary is ",ta)
else:
  ta = x + 0.3*x + 0.95*x
  print("Your Total Salary is ",ta)

  
