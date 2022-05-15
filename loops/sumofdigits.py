'''Program to find the sum of digits of an entered number.'''
x=int(input("Enter the number to be checked "))
sum=0
while x>0 :
    rem=x%10
    sum+=rem
    x//=10
print(sum) 
