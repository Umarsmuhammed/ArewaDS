#Day 14: 30 Days of python programming
#Question 1

#Difference between Map, Filter and Reduce
#Map Function
#The map() function is a built-in function that takes a function and iterable as parameters.
# syntax is 'map(function, iterable)'
#Example
numbers_str = ['1', '2', '3', '4']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))   

#Filter Function
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.
# syntax is filter(function, iterable)
#Example
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
#Reduce Function
#The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value. Example:1
#Example
#numbers_str = ['1', '2', '3', '4', '5']  # iterable
#def add_two_nums(x, y):
 #   return int(x) + int(y)
#total = reduce(add_two_nums, numbers_str)
#print(total)    # 15
#Question2
#Higher-Order Functions: A higher-order function is a function that takes one or 
# more functions as arguments and/or returns a function as its result.

#Python Closures Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure.

#Python Decorator: A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 

#Question 3
class Multiply:
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, value):
        return self.factor * value

multiply_by_2 = Multiply(2)
print(multiply_by_2(5)) # 10

numbers = [2,4,6,8,10]  #map function:
squared_numbers = map(multiply_by_2, numbers)
print(list(squared_numbers)) 

def is_even(value):  #filter function:
    return value % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers)) 

from functools import reduce #Reduce function:
def add(accumulator, value):
    return accumulator + value
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) 

#Question 4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#Question 5
names = ['Umar', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#Question 6
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#Exercise Level 2 
#Question 1
countries = ['Nigeria','Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def to_uppercase(country):
    return country.upper()
uppercase_countries = list(map(to_uppercase, countries))
print(uppercase_countries)

#Question 2
num = [1, 2, 3, 4, 5]
def square(number):
    return number * number
squared_num = list(map(square, num))
print(squared_num)

#Question 3
#names = ['Umar', 'Lidiya', 'Ermias', 'Abraham']
def to_uppercase(name):
    return name.upper()
uppercase_names = list(map(to_uppercase, names))
print(uppercase_names)

#Question 4
countries = ['Iceland', 'Finland', 'Switzerland', 'Thailand', 'Ireland']
def has_land(country):
    return 'land' in country
land_countries = list(filter(has_land, countries))
print(land_countries)

#Question 5
countries = ['Nigeria', 'USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'France', 'Germany', 'Italy', 'Spain', 'Greece']
def has_six_chars(country):
    return len(country) == 6
six_char_countries = list(filter(has_six_chars, countries))
print(six_char_countries)

#Question 6
countries = ['Nigeria', 'USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'France', 'Germany', 'Italy', 'Spain', 'Greece']
def six_or_more_chars(country):
    return len(country) >= 6
six_or_more_char_countries = list(filter(six_or_more_chars, countries))
print(six_or_more_char_countries)

#Question 7
countries = ['France', 'Germany', 'Italy', 'Spain', 'Greece']
def starts_with_e(country):
    return country[0] == 'E'
e_countries = list(filter(starts_with_e, countries))
print(e_countries)

#Question 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))    )
print(squared_even_numbers)

#Question 9
def get_string_lists(lst):
    return list(filter(lambda x: type(x) == str, lst))
mixed_list = ['orange', 'banana', 908, 'mango', 123]
string_list = get_string_lists(mixed_list)
print(string_list)

#Question 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

#Question 11
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries)
sentence = concatenated_countries + " are north European countries"
print(sentence)

#Question 12
def categorize_countries(countries, starts_with):
    return [country for country in countries if country.startswith(starts_with)]
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
countries_starting_with_A = categorize_countries(countries, "A")
print(countries_starting_with_A)

#Question 
def country_letter_count(countries):
    letter_count = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    return letter_count
letter_count = country_letter_count(countries)
print(letter_count)

#Question 15
def get_first_ten_countries(countries):
    return countries[:10]

print('hello world')