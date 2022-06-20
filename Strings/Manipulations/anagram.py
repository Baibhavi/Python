'''Check if a given String is Anagram
'''
a=input("Enter string")
a=a.lower()
b=input("Enter another string")
b=b.lower()
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not Anagram")    