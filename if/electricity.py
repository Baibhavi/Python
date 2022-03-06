'''Write a program to input electricity unit charges and calculate total electricity bill according to the 
	given condition: 
	For first 50 units Rs. 0.50/unit 
	For next 100 units Rs. 0.75/unit 
	For next 100 units Rs. 1.20/unit 
	For unit above 250 Rs. 1.50/unit 
	An additional surcharge of 20% is added to the bill'''
x=int(input("Enter the unit of electricity\n"))
if(x==50):
  bill=50*0.50
  print("The bill is Rs. ",bill)
elif(50<x<=150):
  bill=50*0.50+ (x-50)*0.75
  print("The bill is Rs. ",bill)
elif(150<x<250):
  bill=50*0.50+100*0.75+(x-150)*1.20
  print("The bill is Rs. ",bill)
elif(250<x<500):
  bill=50*0.50+100*0.75+100*1.20+(x-250)*1.50
  print("The bill is Rs. ",bill)
  
  
