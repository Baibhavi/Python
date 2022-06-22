'''Pattern 7
A
B C
D E F
G H I J
K L M N O '''
n=int(input("Enter the number of rows: "))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+count),end=" ")
        count+=1
    print()    