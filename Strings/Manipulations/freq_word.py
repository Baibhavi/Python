'''Find the Frequency of the Word ‘the’ in a given Sentence'''
a=input("Write something")
a=a.lower()
b=input("Write the word whose frequency to be checked:")
b=b.lower()
c=a.count(b)
print("Frequency of ",b ,"is ",c)