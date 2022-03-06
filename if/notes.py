#Write a program to count total number of notes in given amount. 

x=int(input("Enter the amount"))
k2=x//2000
rem1=x%2000
h5=rem1//500
rem2=rem1%500
h2=rem2//200
rem3=rem2%200
h1=rem3//100
rem4=rem3%100
t5=rem4//50
rem5=rem4%50
t2=rem5//20
rem6=rem5%20
t1=rem6//10
print("Total number of notes = ",k2+h5+h2+h1+t5+t2+t1)
