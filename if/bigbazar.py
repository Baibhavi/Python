'''Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the 
shopping amount is greater than 25000, the category is GOLD. If the shopping amount is 
between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The 
discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is 
10% of the shopping amount and 5% otherwise. Design a program in python that asks the user 
to input the total shopping amount, outputs the category and amount to be paid.'''
x=int(input("What is the total amount of your shopping"))
if x>25000 :
  print("Congrats! You fall in Gold category")
  y = x-(x*0.2)
  print(f"You have to pay Rs. {y} only as you got 20% discount")
elif 10000<=x<=25000:  
  print("Congrats! You fall in Silver category")
  y = x-(x*0.1)
  print(f"You have to pay Rs. {y} only as you got 10% discount")
else:
  print("Congrats! You fall in Bronze category")
  y = x-(x*0.05)
  print(f"You have to pay Rs. {y} only as you got 5% discount")
