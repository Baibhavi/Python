'''Program to find the series of all three digits Armstrong numbers.'''
x=int(input("Enter the number to be checked"))
sum=0
s=x
while s>0 :
  digit = s%10
  sum += digit**3
  s//=10
if x==sum:
  print("Armstrong")
else:
  print("Not armstrong")
