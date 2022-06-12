'''Write a program to find sum of all even numbers upto 30 except 10 and 20.'''
sum=0
for i in range (31):
    if i%2==0:
        if i!=10 and i!=20:
            sum+=i
print(sum)            

            