# Length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length = len(it_companies)
print('The length of it_companies is:', length)

# adding twitter to it_companies
it_companies.add('Twitter')
print("The updated list:", it_companies)

# inserting multiple companies
it_companies2 = {'Visteon', 'PWC'}
it_companies.update(it_companies2)
print('After adding multiple companies:', it_companies)

# removing a company
it_companies.remove('PWC')
print('IT companies after removing PWC:', it_companies)

# difference between remove and discard
it_companies.discard('PWC')
print('IT companies after removing PWC:', it_companies)
# In remove() function error will be shown if the item is not fond in set where as discard() will not display any error

# Joining A & B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print('After joining A & B:', C)

# Intersection of two A & B
print('Intersection of A & B', A.intersection(B))

# finding if A subset of B
print("Is A subset of B", A.issubset(B))

# finding if A & B are disjoint sets
print("Is A and B are disjoint sets:", A.isdisjoint(B))

# Joining A with B and B with A
print('Joining A with B', A.union(B))
print('Joining B with A', B.union(A))

# Symmetric difference between A and B
print("The Symmetric difference between A and B:", A.symmetric_difference(B))

# Deleting the sets completely
del A
del B
print('After deleting the sets:', A, B)

# Ages into Set
age = [22, 19, 24, 25, 26, 24, 25, 24]
D = set(age)
agelist = len(age)
ageset = len(D)
print("The length of age list", agelist, "The length of age set", ageset)
if(agelist==ageset):
    print('length is same')
else:
    print('lenght is not same')




