
def string(s): # using function
    u = sum(1 for i in s if i.isupper()) # using is upper function and finding total upper letters
    l = sum(1 for i in s if i.islower()) # using is lower function and finding total lower letters
    print("No. of Upper case characters:", u)
    print("No. of lower case characters:", l)
string('The quick Brow Fox')

