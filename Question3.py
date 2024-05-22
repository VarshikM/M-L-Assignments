# creating a tuple of my sisters and brothers
brother_names = ('Srikar', 'pavan')
sister_names = ('Manvitha' , 'Ishitha')
print(brother_names)
print(sister_names)

# Joining the both tuples to siblings
siblings = brother_names+sister_names
print(siblings)

# Number of siblings
a = len(siblings)
print("The number of siblings are;", a)

# Modifying tuple and adding my parents names
family_members = siblings +('Raja Sekhar' , 'Bindu')
print("Family members are:" , family_members)
