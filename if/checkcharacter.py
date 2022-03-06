#Write a program to check whether a character is alphabet or not. 
x=str(input("Enter the Character\n"))
if((x>='a' and x<='z') or (x>='A' and x<='Z')):
  print(x,"Alphabet")
else:
  print(x,"Not Alphabet")
  
