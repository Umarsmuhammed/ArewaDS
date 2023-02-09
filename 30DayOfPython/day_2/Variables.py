#Day 2: 30 Days of python programming
first_name = 'Umar'
last_name = 'Sani'
full_name = 'Umar Sani Muhammad'
Country = 'Nigeria'
City = 'Kano'
Age = 30
Year = 2023
Is_married = True
is_True = False
is_light_on = True
first_name, last_name, country, age, is_married = 'Umar', 'Sani', 'Nigeria', 30, True

#Exercise Level 2
print(type('Umar'))     # str
print(type(first_name))     # str
print(type(40))             # int
print(type(6.87))           # float
print(type(2 + 3j))         # complex
print(type(False))           # bool
print(type([2, 4, 6, 8]))     # list
print(type({'name':'Umar','age':30, 'is_married':True}))    # dict
print(type((3,5,7)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
#Question 2
print(len('Umar')) 
first_name = len('Umaru')
last_name = len('San')
print(first_name == last_name)  #Alternatively
print(len('Umar') == len('San'))      
#Question 4
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_two * num_one
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)
# Question 5
r, Pi = 30, 3.142  # Radius of circle and value of Pi
Area = Pi * r**2
print(Area)
Circumference = 2*Pi*r
print(Circumference) 
Area2 = Pi*20
print(Area2)
#Question 6
first_name = input('What is your name: ')
last_name = input('What is your Fathers name:')
country = input('Where are you from:')
age = input('How old are you? ')
print(first_name)
print(last_name)
print(country)
print(age)
# Question 7
help('keywords')    # This gives Python reserved words or keywords
