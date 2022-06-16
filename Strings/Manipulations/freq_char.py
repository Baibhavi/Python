'''Find the Frequency of Characters in a String'''

#using function
str=input("Enter the string\n")
char=input("Enter the character to be checked\n")
count=str.count(char)
print(count)

#using loop
str=input("Enter the string\n")
char=input("Enter the character to be checked\n")
count=0
for i in str :
    if i==char:
        count+=1
    else:
        count+=0    
print(count)    
