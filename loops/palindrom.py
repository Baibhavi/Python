#Write a program to find whether a given string or number is palindrome or not
from re import A


a=int(input("Enter the number to be checked"))
n=a
rev=0
while n>0 :
    rem=n%10
    rev=(rev*10)+rem
    n//=10
if a==rev:
    print("Palindrome")
else:
    print("Not Palindrome")       
