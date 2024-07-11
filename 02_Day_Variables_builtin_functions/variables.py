
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name) #First name: Asabeneh 
print('First name length:', len(first_name)) #First name length: 8
print('Last name: ', last_name) #Last name:  Yetayeh
print('Last name length: ', len(last_name)) #Last name length:  7
print('Country: ', country) #Country:  Finland
print('City: ', city) #City:  Helsinki
print('Age: ', age) #Age:  250
print('Married: ', is_married) #Married:  True
print('Skills: ', skills) #Skills:  ['HTML', 'CSS', 'JS', 'React', 'Python']
print('Person information: ', person_info) #Person information:  {'firstname': 'Asabeneh', 'lastname': 'Yetayeh', 'country': 'Finland', 'city': 'Helsinki'}

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name) #First name: Asabeneh
print('Last name: ', last_name) #Last name:  Yetayeh
print('Country: ', country) #Country:  Helsink
print('Age: ', age) #Age:  250
print('Married: ', is_married) #Married:  True

# 2.1 Check the data type of all your variables 

print(type(first_name)) #<class 'str'>
print(type(last_name)) #<class 'str'>
print(type(country)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(is_married)) #<class 'bool'>

# 2.3 Compare length of first name to last name: 
print(len(first_name) - len(last_name)) #(8 - 7) = 1 

# 2.4 Declare 5 as num_one and 4 as num_two
num_one = 5 
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two 
#Ans:9

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
#Ans: -1

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
#Ans: 20

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#Ans: 1.25

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Ans: 4

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Ans: 625

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_devision = num_one // num_two 
#Ans: 1

# 2.5 The radius of a circle is 30 meters.
r = 30
pi = 3.14
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * (r ** 2)
#Ans: 2826.0

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * r
#Ans: 188.4

# Take radius as user input and calculate the area.
pi * (int(input('Enter Radius: ')) ** 2)

# 2.6 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('Country: ')
age = input('Age: ')

# 2.7 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
