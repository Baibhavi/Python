'''Program to display the table of an entered number in the following format:
2*1=2
2*2=4
………..
2*10=20
'''
x=int(input("Enter the number you want table of: "))
for i in range (1,11):
  p=x*i
  print(f"{x} x {i} = {p}")
