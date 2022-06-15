'''Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length 
will be at least 2.
withoutEnd("Hello") → "ell"
withoutEnd("java") → "av"
withoutEnd("coding") → "odin"'''
def withoutEnd(str):
    str2=str[1:len(str)-1:1]
    return str2
a=input("Enter the string")
print(withoutEnd(a))    