'''Find the Number of Vowels, Consonants, Digits and White space in a String'''
str=input("Enter the string")
vowel=0
consonant=0
digit=0
space=0
for i in range (0,len(str)):
    ch=str[i]
    if  (('a'<=ch<='z') or ('A'<=ch<='Z')) :
        ch=ch.lower()
        if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch =='u'):
            vowel+=1
        else:
            consonant+=1
    elif ('0'<=ch<='9'):
        digit+=1
for i in str:
    if i==" ":
        space+=1

print("Vowels=",vowel)
print("Consonants=",consonant)
print("Digits",digit)
print("White spaces=",space)                     