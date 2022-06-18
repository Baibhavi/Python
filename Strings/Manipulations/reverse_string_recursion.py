'''Reverse a Sentence by Recursion'''
def reverse(str1):
    n=len(str1)
    if n==0:
        return str1
    else:
        new=str1[-1:-(n+1):-1]
        return new
a=input("Enter")
print(reverse(a))        