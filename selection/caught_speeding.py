'''caught speeding
You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If 
speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is 
your birthday -- on that day, your speed can be 5 higher in all cases.
-caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0'''

def caught_speeding (speed,is_birthday):
    if is_birthday==False:
        if speed <=60:
            print("No ticket")
            return 0
        elif 60<speed<=80:    
            print("Small ticket")
            return 1
        else  :
            print("Big ticket")
            return 2  
    if is_birthday==True:
        if speed<=65:
            print("No Ticket")
            return 0
        elif 65<speed<=85:
            print("Small ticket")
            return 1
        else:
            print("Big Ticket")
            return 2                   
s=int(input("Enter your speed\n"))
b=input("Is it your birthday? Write True or False\n")
caught_speeding(s,b)         
