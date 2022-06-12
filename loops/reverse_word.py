'''Write a Python program that accepts a word from the user and reverse it'''
a=input("Enter a word\n")
b=a[::-1]
print(b)

#using loop
a=input("Enter a word\n")
for c in range(len(a),0,-1):
    print(a[c],end =" ")
print("\n")    

