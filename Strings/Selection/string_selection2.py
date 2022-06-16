'''Given a string, return a new string where "not " has been added to the front. However, if the string 
already begins with "not", return the string unchanged.
'candy' → 'not candy'
'x' → 'not x'
'not bad' → 'not bad'  '''
def new(str1):
    if str1[0:3:1]=='not' :
        return str1
    else :
        return ('not '+str1)
a=input("Enter string")
print(new(a))            
