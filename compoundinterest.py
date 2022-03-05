p=float(input("Enter the Principle amount to be compounded annually\n"))
r=float(input("Enter the rate of interest\n"))
t=float(input("Enter the time period\n"))
q=(1+0.01*r)**t
ci=p*q - p
a=p*q
print("The compound interest is ",ci)
print("The amount is ",a)
