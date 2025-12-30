"""
for loop is used when you know how many times you want to repeat something or when you want to loop over a collection (range, list, string, etc.).
# syntax:- for var in 'range'( ):
              #print(var)
# syntax:- for var in 'list' [ ]:
               #print(var)
# syntax:- for var in "string" :etc 
                 #print(var)
"""
# loop always print n-1

i = 10
for i in range(1,20):
    print(i)
    #till 19

item = ["banana", "shoes", "chips"]
for item in item:
    print(item)

letters = "anand,kumawat"
for letters in letters:
    print(letters)