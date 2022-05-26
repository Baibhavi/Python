#WAP to convert ᵒC to ᵒF and ᵒF to ᵒC
a=input("You want to convert into fahrenheit or celcius? Write F for fahrenheit and C for celcius")
t=int(input("Enter the temperature"))
if a=='F':
    t1= ((1.8*t) + 32)
    print(t1," Degree Fahrenheit")  
elif a=='C' :
    t1 = ((t - 32)/ 1.8)
else: 
    print("Invalid Input!")    

