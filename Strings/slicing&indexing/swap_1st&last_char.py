'''Given a string, return a new string where the first and last chars have been exchanged.
'code' → 'eodc'
'a' → 'a'
'ab' → 'ba'''

def new_str(str1):
    x=str1[-1]
    y=str1[1:len(str1)-1:1]
    z=str1[0]
    if len(str1)>1:
        return x+y+z
    elif len(str1)==1:
        return str1    
a=input("Enter string")
print(new_str(a))        