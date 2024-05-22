# Taking input from user for number of inputs
N = int(input("Enter the number of student weights you want to enter"))
weight_in_lbs = []

# using for loop for taking input
for i in range(N):
    weights = float(input(f"Enter student {i +1} weight:"))
    weight_in_lbs.append(weights)
    print("The given weights in lbs are:", weight_in_lbs)
# creating an empty list
weight_in_kgs = []
for weights in weight_in_lbs:

   # converting lbs into kgs
    weight_in_kg = weights*0.453592
    weight_in_kgs.append(weight_in_kg)

    print(weight_in_kgs)




