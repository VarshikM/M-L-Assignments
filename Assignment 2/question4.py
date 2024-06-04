def sample_list(l):
  x = [] # creating an empty list
  for a in l:
    if a not in x:
      x.append(a)  # using append function
  return x
print("Unique List:", sample_list([1,2,3,3,3,3,4,5]))
