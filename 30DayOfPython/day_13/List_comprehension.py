#Day 13: 30 Days of python programming
#Question 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)

#Question 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)

#Question 3
list_of_tuples = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# Question 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(flattened_list)

# Question 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dicts = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(list_of_dicts)

# Question 6
names = [[('Umar', 'Sani')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_strings = [name[0][0] + " " + name[0][1] for name in names]
print(concatenated_strings)

# Question 7
cal_slope_or_intercept = lambda x, y, slope_or_intercept: x * y if slope_or_intercept == "slope" else y
result = cal_slope_or_intercept(2, 3, "slope")
print("Slope:", result)
result = cal_slope_or_intercept(2, 3, "intercept")
print("Y-intercept:", result)


