'''Remove all Characters in Second String which are present in First String
'''
str1=input("Write a word")
str2=input("Write another word")
b=""
for i in str2:
    if (i not in str1):
        b=b+i
print(b)        



