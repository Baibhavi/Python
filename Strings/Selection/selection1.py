'''Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, 
the front is whatever is there. Return a new string which is 3 copies of the front.
'Java' → 'JavJavJav'
'Chocolate' → 'ChoChoCho'
'abc' → 'abcabcabc'
'''
def new (str1):
    a=str1[0:3:1]
    if len(str1)>3:
        return a*3
    else:
        return str1*3
x=input("Enter the string")
print(new(x))          
