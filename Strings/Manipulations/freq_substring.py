'''Frequency of Substring in the given String'''
s=input("Enter string")
s=s.lower()
sub_S=input("The substring to be checked?")
if sub_S in s:
    c=s.count(sub_S)
else:
    c='Invalid Input'
print(c)