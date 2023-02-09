# Day 9: 30 days of python programmings

a = int(input('Enter your age: '))  # user input using if statement
if a >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18-a} more years to learn to drive')

my_age = 28
your_age = int(input('Enter your age:'))

if my_age > your_age:
    if my_age - 1 == your_age:
        print("I am one year older than you")
    else:
        print(f'I am {my_age - your_age} years older than you')
elif my_age < your_age:
    if my_age + 1 == your_age:
        print('You are one year older than me')
    else:
        print(f'You are {your_age - my_age} years older than me')
else:
    print('We are the same age')

a = int(input('Enter number one:'))
b = int(input('Enter number two:'))
if a < b:
    print('a is smaller than b')
elif a > b:
    print('a is greater than b')
else:
    print('a is equal to b')

score = 60
if score <=100 and  score >= 90:
    print("A")
elif score <= 89 and score >= 70:
    print("B")
elif score <=69 and score >= 60:
    print("C")
elif score <= 59 and  score >= 50:
    print("D")
else:
    print("F")

#Seasons
user_input = 'December'
if user_input == 'September' or user_input == 'October' or user_input == 'November':
    print("The season is Autumn")
elif user_input == 'December' or user_input == 'January' or user_input == 'February':
    print('The season is Winter')
elif user_input == 'March' or user_input == 'April' or user_input == 'May':
    print('The season is Spring')
else:
    print('The season is Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = 'apple'
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else: 
    print('The fruit already exists in the list')
person = { 
	'first_name': 'Umar', 
	'last_name': 'Muhammad',
	'age': 30, 
	'is_married': True,
	'skills': ['React', 'Javascript', 'MongoDB', 'Node', 'Python'],
	'country': 'Nigeria',
	'address': {
				'Naibawa street'
				'zipcode': '0909'
	}
	}

'''Check if the person dictionary has skills key, 
    if so print out the middle skill in the skills list.'''
if 'skills' in person:
    skills_length=len(person['skills'])
    if skills_length%2==0:
        middle_element=person['skills'][int(((skills_length/2)-1)) : int(((skills_length/2))+1)] 
        print('The middle skill :',middle_element)
    else:
        middle_element2=person['skills'][skills_length//2] 
        print('The middle skill :',middle_element2)

'''Check if the person dictionary has skills key, if so check if the person has 'Python' skill
and print out the result.'''
if 'skills' in person:
	print('The person have skills')
	check = 'Python' in person['skills']
	if check is True:
		print('\'Python\' is in skills')
	else:
		print('not in skills')
else:
	print('The person doesn\'t have skills')


'''If a person skills has only JavaScript and React, print('He is a front end developer'),
if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
else print('unknown title') - for more accurate results more conditions can be nested!'''

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
       print('He is a front end developer')
elif 'Node' in person['skills'] and 'python' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MangoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('Unknown skills!')
