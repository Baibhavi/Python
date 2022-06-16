'''Given a string, return a "rotated right" version where the last n chars are moved to the start. The string 
length will be at least 2.
right2("Hello",2) → "loHel"
right2("java",3) → "avaj"
right2("Hi",3) → "Hi" '''
def right2(str1,n):
    str2=str1[-2]
    str3=str1[-1]
    str4=str1[0:len(str1)-n:1]
    if len(str1)>2 :   
        return str2+str3+str4
    elif  len(str1)==2:
        return str2+str3
a=input("Enter the string\n")
b=int(input("Number of char upto which is should be rotated\n"))
print(right2(a,b))
