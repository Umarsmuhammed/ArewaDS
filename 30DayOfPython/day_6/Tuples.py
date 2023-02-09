# Day 6: 30 days of python programming
#Exercise Level 1
# Create an empty tuples
emp_tpl = tuple() 
emp_tpl2 = ()  

# Create two tuples each containing names of your sisters and your brothers (imaginary siblings are fine)
my_bros = ('Shamsu','Ahmad', 'Mustapha')
my_sis = ('Hadiza','Aisha','Hassana')
siblings = my_bros + my_sis  ## Join tuples and call it siblings
print(siblings)
print(len(siblings)) # number of siblings

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)  #Modifying siblings
parents = ['Sani','Rabiatu']
family_members = siblings
print("Family_members: ",family_members)


#Exercise Level 2
# Unpacking siblings and parents
*sib,father, mother = family_members
print(sib)  # sibs = siblings unpacked
a,b,c,d,e,*paren = family_members
print(paren)  # pare = parents unpacked

fruits = ('Banana','Orange','Apple')  #Join the three tuples
vegetables = ('Onion','Tomato')
animal_products = ('Meat','liver','Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_list = list(food_stuff_tp) ## Change tuples name from food_stuff_tp tuple to a food_stuff_lt list

len(food_stuff_tp)
food_stuff_tp[int(len(food_stuff_tp)/2)-1:int(len(food_stuff_tp)/2)+1] # slice out the middle item

food_stuff_list[0:3]  # Slice out the first three and the last three items
food_stuff_list[-3:]  # last three

del food_stuff_tp  # Delete the food_staff_tp tuple 
print(food_stuff_list)  #

# Check if an item exists in tuple:
'Orange' in food_stuff_tp # Errors, food stuff tupple no longer exists

'Orange' in food_stuff_list # True
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden') #creating a list
'Estonia' in nordic_countries # false
'Iceland' in nordic_countries  # True 

