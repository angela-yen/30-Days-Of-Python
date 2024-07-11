# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# 1. Declare your age as integer variable
age = 28

# 2. Declare your height as a float variable
height = 173.5

# 3. Declare a variable that store a complex number
complex_number = 1 + 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = input('Enter base:' )
height = input('Enter height: ')
area = 0.5 * int(base) * int(height)
print('The area of the triangle is ', area)

    # Enter base: 20
    # Enter height: 10
    # The area of the triangle is 100

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print('The perimeter of the triangle is ', perimeter)

# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = input('Enter length: ')
width = input('Enter width: ')
area = int(length) * int(width)
print('Area: ', area)
 
primeter = 2 * int(length) * int(width)
print('Perimeter: ', perimeter)

# 7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input('Enter Radius: ')
pi = 3.14
area = pi * (int(radius) ** 2)
circumference = 2 * pi * int(radius)
print('Area ', area)
print('Cicumference ', circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_a = -2
x_int = (0, -2)
y_int = (1, 0)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope_b = (10 - 2)/(6-2)
distance = ((4**2) + (8**2)) * 0.5
# 10. Compare the slopes in tasks 8 and 9.
print(slope_a == slope_b)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
print('on' in 'dragon')

print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'python')

# 16. Find the length of the text python and convert the value to float and convert it to string
to_float = float(len('python'))
to_string = str(to_float)

print(len('python'))
print(float(len('python')))
print(to_string)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = int(input('Enter x:'))

output = x % 2 == 0

print('X is even', output)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print( 7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print(int('9.8') == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')
print('Your weekly earning is: ', int(hours) * int(rate))

# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = input('Enter number of years you have lived: ')
print('You have lived for ', int(years) * 31556952, 'seconds.')

# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

# 23. Write a Python script that displays the following table
print([[1,1,1,1,1], [2,1,2,4,8], [3,1,4,9,27], [4,1,4,16,64], [5,1,5,25,125]])

print(' 1 1 1 1\n 2 1 2 4 8\n 3 1 3 9 27\n 4 1 4 16 64\n 5 1 5 25 125')
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125