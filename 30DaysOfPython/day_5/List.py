# Day 5: 30 days of python programming
#Exercise Level 1
# Declare an empty list
list_a = list()
list_b = []
print(f' the lists are {list_a},{list_b}')

My_list = ['Ammar','Nasreen','Ibrahim','Aliyu','Zainab','Umar'] # Declaring a list
list_length = len(My_list)  # length of my list
print(f'The length of my list is {list_length}') 

# first, middle and last item of my list
first_item =  My_list[0] 
middle_item =  My_list[int(len(My_list)/2)] 
last_item =  My_list[-1]  
print(f'The first, middle and last items in the list are {first_item},{middle_item} and {last_item} respectively ')

mixed_data_types = ['Umar', 30, 1.68,'Married','Kano'] #Mixed data containing my information

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] #IT companies

print(IT_companies)
print(mixed_data_types)
length_comp = len(IT_companies)
print(len(mixed_data_types))
# index of  first, middle and last company
first_comp = IT_companies[0] # first : Facebook
middle_comp = IT_companies[len(IT_companies)//2] # middle: Apple
last_comp = IT_companies[-1] # last: Amazon
print(f'The first middle and last companies are {first_comp},{middle_comp} and {last_comp} respectively.')
IT_companies[0] = 'Techno' # modifying one of the companies list
print(IT_companies)

IT_companies.insert(0,'Google')  # take  Google back to position one
print(IT_companies)

IT_companies.insert(len(IT_companies)//2,'Zipline') # Inserting an IT company in the middle of the list
print(IT_companies)

IT_companies[1] = IT_companies[1].upper()  # Change one to uppercase (IBM excluded!)
print(IT_companies)

'#,' .join(IT_companies)

IT_company = ['Apple', 'IBM', 'Oracle', 'Amazon']
does_exist = 'Oracle' in IT_company
print(does_exist)  # To Check for an existing company

# Sort the list using sort() method
IT_companies.sort() # method returns none
print(IT_companies)

# Reverse the list in descending order using reverse() method
IT_companies.reverse() # 
print(IT_companies)

IT_companies[:3]  # Slice out the first 3 companies from the list

IT_companies[-3:]   # Slice out the last 3 companies from the list

IT_companies[len(IT_companies)//2:len(IT_companies)//2+1]   # Slice out the middle IT company or companies from the list

IT_companies.pop(0)   # Remove the first IT company from the list

IT_companies.pop(int(len(IT_companies)/2))   # Remove the middle IT company or companies from the list

IT_companies.pop()  # Remove the last IT company from the list

IT_companies.clear()  # Remove all IT companies from the list

del IT_companies  # Destroy the IT companies list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)  # Join the lists:

full_stack = front_end.copy() # front_end contains the two lists, but first find the index of redux

full_stack.index('Redux')  # Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack.insert(5,'Python') # insertion is done before the index

full_stack.insert(full_stack.index('Python')+1,'SQL')


## Exercise Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()  # Sort the list and find the min and max age
print(ages)
min_age = min(ages)  
max_age = max(ages)  
print(f'The minimum age is {min_age} and the maximum age is {max_age} ')
ages.extend([19,26])  # Add the min and the max to the list

ages.sort()
ages_length = len(ages)
len(ages)
print(ages[int(len(ages)/2-1)],ages[int(len(ages)/2)]) 

if ages_length % 2 == 0:
  cond1 = ages[ages_length//2]
  cond2 = ages[ages_length//2-1]
  median_age = (cond1 + cond2)/2

else: 
  median_age = ages[ages_length//2]
print(f'The median age of the ages is {median_age}')

average = sum(ages)/len(ages) # 22.75 #average age is the sum of all items divided by their number )
print(f'The average age is {average}')

range = max(ages) - min(ages) # the range of the ages (max - min)
print(f'The range of the ages is {range}')

abs(min(ages) - average) == abs(max(ages)- average) #Compare the values

# to find the middle country(ies) in the countries list
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
]
countries.sort()
countries_length = len(countries)

if countries_length % 2 == 0:
  cnd1 = countries[countries_length//2]
  cnd2 = countries[countries_length//2-1]
  middle_country = (cnd1 , cnd2)

else: 
  middle_country = countries[countries_length//2]
print(f'The mid country in the countries list is {middle_country}')
countries_length = len(countries) 
first_half = countries[:countries_length//2]
second_half = countries[countries_length//2:]
first_half_length = len(first_half)
second_half_length = len(second_half)

print(f'The length of the two halves are {first_half_length} and {second_half_length} ')

# Unpacking of list of  the first three countries and the rest as scandic countries.
CH,RU,US,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic
print(f'The scandic countries in the last list given are {scandic}')
