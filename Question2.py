# creating an empty dictionary
dog = {}
print(dog)
# adding to dictionary
dog = {"name": "brownie", "color": "brown", "breed": "chow-chow", "legs": "4", "age": "3"}
print("The updated dog dictionary:", dog)
# creating a student dictionary
student = {"first_name": "Suraj", "Last_name": "Gamini", "gender": "male", "age": "22", "marital_status": "single", "skills": ["Programming"], "Country": "India", "City": "Tanuku", "address": "ws/dw/12"}
student1 = student.keys()
print("The keys of dictionary student is:", student1)
# Length of student dictionary
length = len(student)
print(length)
# getting the values of a particular key in dictionary
print(student["skills"])
# Modifying dictionary
student["skills"].extend(["Leadership", 'cricket'])
print(student['skills'])
# getting dictionary keys
key_List = list(student.keys())
print(key_List)
# getting values as a list
value_list =list(student.values())
print(value_list)

