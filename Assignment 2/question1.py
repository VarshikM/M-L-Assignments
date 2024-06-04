
for i in range(1, 6):
    for j in range(i): # inner loop runs from 0 to i, where i is the current iteration of the outer loop
        print("*",end="")
    print("")
for i in range(4, 0, -1): # loop starts from 4 and goes till 0 with a step of -1, thus it prints the reverse pattern.
    for j in range(i):
        print("*",end="")
    print("")


