
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty '
b = 'Days '
c = 'Of '
d = 'Python'

print(a + b + c + d)
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = 'Coding '
b = 'For '
c = 'All'

print(a + b + c)
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
company.upper()

# 7. Change all the characters to lowercase letters using lower() method.
company.lower()

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company.capitalize()
company.title()
company.swapcase()

# 9. Cut(slice) out the first word of Coding For All string.
company[7:15]

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string =  'Coding'
print(company.index(sub_string))

print(company.find('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace(company, 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
var = 'Python for Everyone'
print(var.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
var = 'Coding for All'
print(var.split(' '))
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
var = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(var.split(','))

# 15. What is the character at index 0 in the string Coding For All.
var = 'Coding For All'
print(var[0])

# 16. What is the last index of the string Coding For All.
print(var[-1])

# 17. What character is at index 10 in "Coding For All" string.
print(var[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
abb = name.split(' ')
ans = abb[0][0] + abb[1][0] + abb[2][0]

print(ans)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
name = 'Coding For All'

abb = name.split(' ')
ans = abb[0][0] + abb[1][0] + abb[2][0]

print(ans)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
var = 'Coding For All'

var.index('C')

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
var.index('F')

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
var = 'Coding For All People'
var.rfind('l')

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'

sentence.find('because')

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence.rfind('because')

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence[31:54]

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence.find('because')

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence[31:54]

# 28. Does ''Coding For All' start with a substring Coding?
substring = 'Coding'
var = 'Coding For All'

print(var.index(sub_string))

# 29. Does 'Coding For All' end with a substring coding?
substring = 'coding'

print(var.endswith(sub_string))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
var = '   Coding For All      '
var.strip()

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

var_1 = '30DaysOfPython'
var_2 = 'thirty_days_of_python'
var_1.isidentifier()
# False
var_2.isidentifier()
# True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
ans = ' '.join(lib)
print(ans)

# 33. Use the new line escape sequence to separate the following sentences
# I am enjoying this challenge.
# I just wonder what is next.

print('I\n am\n enjoying\n this\n challenge.')
print('I\n just\n wonder\n what\n is\n next.')

# 34. Use a tab escape sequence to write the following lines

# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print('Name\t Age\t Country\t City')
print('Asabeneh\t 250\t Finland\t Helsinki')

# 35. Use the string formatting method to display the following:
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

formatted_string = 'The area of a circle with radius {} is {} meters square'.format(radius, area)
print(formatted_string)

# 36. Make the following using string formatting methods:

# 8 + 6 = 14
a = 8
b = 6 
c = a + b
print('{} + {} = {}'.format(a, b, c))

# 8 - 6 = 2
d = a - b 
print('{} - {} = {}'.format(a, b, d))

# 8 * 6 = 48
e = a * b
print('{} * {} = {}'.format(a, b, e))

# 8 / 6 = 1.33
f = a / b
print('{} / {} = {:.2f}'.format(a, b, f))

# 8 % 6 = 2
g = a % b
print('{} % {} = {}'.format(a, b, g))

# 8 // 6 = 1
h = a // b
print('{} // {} = {}'.format(a, b, h))

# 8 ** 6 = 262144
i = a ** b
print('{} ** {} = {}'.format(a, b, i))
