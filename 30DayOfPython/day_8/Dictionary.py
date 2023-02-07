# Day 8: 30 days of python programming

dog = dict()   #empty dictionary
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Umar'
dog['color'] = 'Pink'
dog['breed'] = 'Hunter'
dog['legs'] = 4
dog['age'] = 3

student = dict()  # Create a student dictionary and add some information
student.update({'first_name': 'Umar', 'last_name': 'Muhammad','gender': 'male','age': 30,'marital_status': 'married','skills':['Excel','Matlab','Python'], 'country':'Nigeria','city': 'Kano','address': 'No. 78 Kawon Arewa'})

print('length of student dict: ', len(student)) ## length of the student dictionary

student['skills']
print(type(student['skills']))   # list

student['skills'].append('Web design') # Modifying the skills
print('Updated skills:', student)

print('dictionary keys as a list: ',student.keys())   # Get the dictionary keys as a list

print('dictionary value as a list: ',student.values())  # Get the dictionary values

print('list of tuples of dict items: ',student.items()) # using items() method

# Delete one of the items in the dictionary
student.pop('gender')

del student  # delete one of the dictionaries
print(student) # Return Error

