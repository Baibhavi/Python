a=int(input("Enter the amount to be withdrawn\n"))
a1=a-100
k2=a1//2000
rem=a1%2000
h5=rem//500
rem2=rem%500
h1=rem2//100
print("Number of minimum notes required",k2+h5+h1+1)
print("Number of 2000 notes = ",k2)
print("Number of 500 notes = ",h5)
print("Number of 100 notes = ",h1)
