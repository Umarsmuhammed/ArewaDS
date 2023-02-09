#Day 3: 30 Days of python programming
my_age = 40
print('my_age', my_age)
my_height = float(14)
print('my_height', my_height)
comp_num = 2+6j
print('complex number', comp_num )
Base = 10
Height = 20
Area_of_triangle = 0.5*Base*Height    
print(Area_of_triangle)     #To calculate Area of triangle
#Alternatively
input('Enter base: 10')
input('Enter height:20')
input('The Area of a Circle is:100')       #To calculate Area of triangle
a = input('Enter side a:')
b = input('Enter side b:')
c = input('Enter side c:')
perimeter = a+b+c
print('The perimeter of the triangle is:', perimeter)

#No 6. Tp find the length and width of a rectangle using prompt. 

#length =input('Enter length of rectangle:', )
#breadth = input('Enter breadth of rectangle:,')
#area = length * breadth
#print('The area of the rectangle is' ',area',  'square meters')

# To calculate the radius and circumference of a circle using prompt,  pi = 3.14
#import math
#r = input("the radius of the circle is: ")
#area = math.pi * r ** 2
#perimeter = 2 * math.pi * r 
#print("The area of the circle is: ",area, " and ", "the perimeter is : ", perimeter)

# to calculate the slopeof the equation y = 2x -2
# when y = 0 what is the corresponding value of x 
# when x = 0 what is the corresponding value of y
y = 2 * 0 - 2
x = ( 2 * 0 ) / 2
print("The x-intercept of y = 2x-2 is: ",x, " and ", "the y-intercept is: ", y)

# To find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1,y1,x2,y2 = 2,2,6,10
m = (y2 - y1) / (x2 - x1)
# euclidean distance,d =  square root of squared distances
d2 = ((y2 - y1) ** 2) + ((x2 - x1) ** 2 )
d = math.sqrt(d2)
print("The slope is: ", m, "and the Euclidean distance is:" ,d)

# Comparison between the slopes in tasks 8 and 9.
# The gradient for the task 8 is 2 and that for task 9 is 4
# using code, I'll let the slope for task 8 to be m0 since that for task 9 is m
m_1 = 2
m_2 = 4
print("Equal: ", m_1==m_2, "Unequal: ", m_1!=m_2)
# checking which is greater or less
print("Greater than: ", m_1==m_2, "Less than: ", m_1==m_2)


# this is quadratic equation y = x^2 + 6x + 9, the solution is x=-3twice
x=-3
y = x ** 2 + 6 * x + 9
print("the value of y: ", y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Length of python: ", len('python'), "length of dragon: ", len('dragon'))
print("Definitely false: ", len('python')> len('dragon'))

# this is contradiction
print(len('python') != len('dragon'))      

#D={dragon}
#A={python}
#is_on in D

# Find the length of the text python and convert the value to float and convert it to string
x = len('python')
y = float(x)
z = str(x)
print("Length, float and string: ",x,y,z)

# using the modulos operator, which gives the remainders,
x = 5
print("x is even: ", x%2==0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print("Checking: ", 7 // 3 == 2.7) # definitely not!!!


# Check if type of '10' is equal to type of 10
#print("Cheking again!: ", type('10')== type(10)) # not equal, of course!

# Check if int('9.8') is equal to 10
#print("Checking yet again: ", int('9.8') == 10) # it raised a ValueError: invalid literal for int() with base 10: '9.8

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
x = 40
y = 28
z = x * y
x = input("Enter hours per week: 2")
y = input("Enter rate per hour: 4")
print("Your weekly earning is: ", z)

# how to calculate the number of seconds a person can live. Assume a person can live 100 years
My_age = 100
Days = My_age * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60
print('Enter number of years you have lived:', My_age, 'years')
print('You have lived for:', Seconds, 'second')


# Write a Python script that displays the following table
print(1, 1, 1, 1, 1) 
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4 ,16 ,64)
print(5, 1 ,5 ,25, 125)
