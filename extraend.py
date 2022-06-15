'''Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string 
length will be at least 2.
extraEnd("Hello") → "lololo"
extraEnd("ab") → "ababab"
extraEnd("Hi") → "HiHiHi" '''
def extraEnd (a):
    b=a[len(a)-2:len(a)+1:1]
    print(b)
    print(len(a)-2)
    return b*3
a=input("Enter the string")
print(extraEnd(a))    