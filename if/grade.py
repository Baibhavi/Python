'''Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following: 
	Percentage >= 90% : Grade A 
	Percentage >= 80% : Grade B 
	Percentage >= 70% : Grade C 
	Percentage >= 60% : Grade D 
	Percentage >= 40% : Grade E 
	Percentage < 40% : Grade F '''

a=int(input("Enter the marks of first subject"))
b=int(input("Enter the marks of second subject"))
c=int(input("Enter the marks of third subject"))
d=int(input("Enter the marks of fourth subject"))
e=int(input("Enter the marks of fifth subject"))
per=(a+b+c+d+e)/5
if(per>=90):
  print("Grade A")
elif(per>=80):
  print("Grade B")
elif(per>=70):
  print("Grade C")
elif(per>=60):
  print("Grade D")
elif(per>=40):
  print("Grade E")
else:
  print("Grade F")




