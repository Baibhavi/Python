#Program that calculates the number of rectangular tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the user.

l1=int(input("Enter the length of a tile\n"))
b1=int(input("Enter the breadth of a tile\n"))
l2=int(input("Enter the length of the floor\n"))
b2=int(input("Enter the breadth of a floor\n"))
d1=l1*b1
d2=l2*b2
print("Number of tiles required to cover the floor", d2/d1)

