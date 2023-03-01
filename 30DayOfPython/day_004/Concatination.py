# Day_4 of 30 days python challenge
# we concatenate the string by joining them together to a single string
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Here we concatenate by joining the string together
print(' '.join(['Coding','for','all']))

# Declare a string variable and print it
company = 'Coding For All'
print(company)

print(len(company)) # Print the length of the string name 'company'

print(company.upper())  # Change all the characters to uppercase letters

print(company.lower())  # Change all the characters to lowercase letters

print(company.capitalize()) # to format the string value using capitalize(), title(), swapcase() methods  
company.swapcase(),
company.title()

statement = 'Coding For All'
first_word = statement[0:6] # starts at zero index and up to 3 but not include 3
print(first_word) # this cut(slice) 

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('Using .index(): ', statement.index('Coding')) 
print('Using .rindex(): ', statement.rindex('Coding')) 
print('Using .find(): ', statement.find('Coding')) 

# Replace the word coding to Python
print(statement.replace('Python','Coding'))

# form the statements replace Everyone with all
print('Python for everyone'.replace('everyone','all'))

# Split the string 'Coding For All' using space as the separator (split()) 
print('Coding For All'.split())
# split the string using comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# character at index 0 in the string Coding For All ?
print(statement[0]) # letter C

# What is the last index of the statement
print(statement[-1])   

# What character is at index 10 in "Coding For All" string ?
print(statement[10])    # space

# Create an acronym or an abbreviation for the name 'Python For Everyone'
statemen2 = 'python for everyone'
letters = statemen2.split()
acc = ''
for i in letters:
    acc+= i[0] + '.'
print('Accronym: ',acc)

#ccf is an acronym for  'Coding For All'
cfa = 'Coding For All'
#to determine the position of the first index in Coding For All
print(cfa.index('C'))    # 0
#to determine the index of the first occurrence.
print(cfa.index('F')) # 7

#to determine last occurrence we use rfind.
print('Coding For All People'.rfind('l'))  # 19

# index of the following sentence: 
statement3 = 'You cannot end a sentence with because because because is a conjunction'
print(statement3.find('because'))  #31

# we use rindex for last occurrence
print(statement3.rfind('because'))   #47

# Slice out the phrase 
print(statement3[31:47 + len('because')])

# to check wether the statement 'Coding For All' start with a substring Coding
print(cfa.startswith('Coding')) 
#to check wether the statement 'Coding For All' end with a substring coding
print(cfa.endswith('coding'))  

string = '   Coding For All      '  # better to assign, less mistakes
print(string.rstrip())  #left and right identation of string.

#boolean means its either true or false
print('30DaysOfPython: ','30DaysOfPython'.isidentifier()) # False 
print('thirty_days_of_python: ','thirty_days_of_python'.isidentifier()) # True

# from python libraries given Join the list with a hash with space string. 
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print('I am enjoying this challenge.\nI just wonder what is next.') # \n indicates next line

print('Name\tAge\tCountry\tCity')   #tab escape sequence
print('Umar\t30\tNigeria\tKano')

# string formatting method to calculate area of a circle:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# by using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
