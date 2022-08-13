#Concatenate two list index-wise
l1=['M','o']
l2=['y','n']
l3=[i + j for i,j in zip (l1,l2)]
print(l3)
