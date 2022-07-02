'''Create a dictionary on the basis of roll no. , name and marks of five subjects .
Also find out sum of all five subjects of a student'''

d={}
s=int(input("Enter the number of students: "))
d1={}
sum=0
for i in range(s):
    r=int(input("Enter the roll number of the student: "))
    k=input("Enter the name of the student: ")
    for j in range(5):
        m=int(input("Enter the marks of first subject: "))
        sum+=m
        d1.update({k:sum})
    d.update({r:d1})
print(d)   
